from qiskit import QuantumCircuit

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
oracle = simon_oracle(secret)
print(oracle.draw())
print(f"\nOracle built for secret string s = {secret}")