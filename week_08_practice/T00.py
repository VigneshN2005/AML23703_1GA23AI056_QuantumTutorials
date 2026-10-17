from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n = 3
qc = QuantumCircuit(n + 1, n)
qc.x(n)
qc.h(range(n + 1))
qc.x(n)                      # oracle: constant f(x)=1
qc.h(range(n))
qc.measure(range(n), range(n))
print(qc.draw())

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
print("Counts:", counts)
print("Constant" if max(counts, key=counts.get) == "000" else "Balanced")