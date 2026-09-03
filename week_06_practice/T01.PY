from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def simon_oracle(s):
    n = len(s)
    qc = QuantumCircuit(2 * n)
    for q in range(n):
        qc.cx(q, q + n)
    if '1' in s:
        i = s[::-1].find('1')
        for q in range(n):
            if s[::-1][q] == '1':
                qc.cx(i, q + n)
    return qc

secret = '110'
n = len(secret)

qc = QuantumCircuit(2 * n, n)
qc.h(range(n))
qc.compose(simon_oracle(secret), inplace=True)
qc.h(range(n))
qc.measure(range(n), range(n))

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()

print(f"Secret string: {secret}")
print(f"Measurement counts: {counts}")