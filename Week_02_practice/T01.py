from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)

sv = Statevector.from_instruction(qc)
plot_bloch_multivector(sv)
