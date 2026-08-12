from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc=QuantumCircuit(5)

qc.x(0)
qc.x(1)

qc.cx(0,3)
qc.cx(1,3)
qc.cx(2,3)

qc.ccx(0,1,4)
qc.ccx(0,2,4)
qc.ccx(1,2,4)

state=Statevector.from_instruction(qc)

print(state)