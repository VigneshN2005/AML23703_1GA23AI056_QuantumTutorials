from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
num_shots = 1024
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
print(qc.draw())
simulator = Aer.get_backend("aer_simulator")
transpiled_qc = transpile(qc, simulator)
job = simulator.run(transpiled_qc, shots=num_shots)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)
plot_histogram(counts)
plt.savefig("Output_T01_Medium.png")
plt.show()
