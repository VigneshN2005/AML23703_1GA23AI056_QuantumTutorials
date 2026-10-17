from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 1)
qc.x(1)
qc.h([0, 1])
qc.cx(0, 1)          # oracle for f(x)=x
qc.h(0)
qc.measure(0, 0)
print(qc.draw())

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
result = max(counts, key=counts.get)
print("Counts:", counts)
print("Result:", result, "->", "constant" if result == "0" else "balanced")