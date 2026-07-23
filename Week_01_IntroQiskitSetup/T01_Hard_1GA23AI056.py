from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
num_qubits = 3
num_shots = 1024
qc = QuantumCircuit(num_qubits, num_qubits)
qc.h(range(num_qubits))
qc.measure(range(num_qubits), range(num_qubits))
print(qc.draw())
simulator = Aer.get_backend("aer_simulator")
transpiled_qc = transpile(qc, simulator)
job = simulator.run(transpiled_qc, shots=num_shots)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)
num_outcomes = 2 ** num_qubits
theoretical_probability = 1 / num_outcomes
print(f"Theoretical probability per outcome: {theoretical_probability:.4f}")
print("Observed probability per outcome:")
for outcome in sorted(counts.keys()):
    observed_probability = counts[outcome] / num_shots
    print(f"  {outcome}: {observed_probability:.4f}")
plot_histogram(counts)
plt.savefig("Output_T01_Hard.png")
plt.show()
