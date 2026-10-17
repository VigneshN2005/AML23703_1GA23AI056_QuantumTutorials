from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()

def dj_oracle(n, kind):
    qc = QuantumCircuit(n + 1)
    if kind == "constant":
        qc.x(n)
    else:
        for i in range(n):
            qc.cx(i, n)
    return qc

def run_dj(n, kind):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.compose(dj_oracle(n, kind), inplace=True)
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return sim.run(transpile(qc, sim), shots=1024).result().get_counts()

print(f"{'n':>2} | {'oracle':>9} | {'result':>8} | verdict")
for n in range(2, 6):
    for kind in ["constant", "balanced"]:
        counts = run_dj(n, kind)
        result = max(counts, key=counts.get)
        verdict = "constant" if result == "0" * n else "balanced"
        print(f"{n:>2} | {kind:>9} | {result:>8} | {verdict}")