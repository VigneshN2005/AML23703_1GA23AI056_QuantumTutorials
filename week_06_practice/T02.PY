from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import itertools

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

secret = '1011'
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

# Solve y . s = 0 (mod 2) for all measured y, brute-force over candidate s
ys = [[int(b) for b in y] for y in counts if '1' in y]
candidates = []
for bits in itertools.product([0, 1], repeat=n):
    if any(bits) and all(sum(a * b for a, b in zip(y, bits)) % 2 == 0 for y in ys):
        candidates.append(''.join(map(str, bits)))

print(f"\nCandidate secret string(s): {candidates}")
print(f"Recovered correctly: {secret in candidates}")