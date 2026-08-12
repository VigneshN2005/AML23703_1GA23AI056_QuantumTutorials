from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc=QuantumCircuit(1)
qc.h(0)

state=Statevector.from_instruction(qc)

p0=abs(state.data[0])**2
p1=abs(state.data[1])**2

print("Heads (0):",p0)
print("Tails (1):",p1)

if p0>p1:
    print("Heads more likely")
elif p1>p0:
    print("Tails more likely")
else:
    print("Fair coin")