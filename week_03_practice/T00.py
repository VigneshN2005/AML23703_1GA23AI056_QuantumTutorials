from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc1=QuantumCircuit(1)
qc1.x(0)
print("X Gate:")
print(Statevector.from_instruction(qc1))

qc2=QuantumCircuit(1)
qc2.y(0)
print("\nY Gate:")
print(Statevector.from_instruction(qc2))

qc3=QuantumCircuit(1)
qc3.z(0)
print("\nZ Gate:")
print(Statevector.from_instruction(qc3))