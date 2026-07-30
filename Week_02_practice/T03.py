import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.h(0)

error_angle = random.uniform(-0.3, 0.3)
qc.p(error_angle, 0)

sv = Statevector.from_instruction(qc)
plot_bloch_multivector(sv)
