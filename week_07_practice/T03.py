import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace

qc = QuantumCircuit(2)
qc.h(0)              # control in |+>
qc.x(1)
qc.h(1)              # target in |->

before = partial_trace(Statevector.from_instruction(qc), [1])
qc.cx(0, 1)          # oracle f(x)=x
after = partial_trace(Statevector.from_instruction(qc), [1])

print("Control qubit BEFORE oracle:\n", np.round(before.data, 3))
print("Control qubit AFTER oracle:\n", np.round(after.data, 3))

print("\nLabel f(x) -> phase (-1)^f(x)")
for x in [0, 1]:
    print(f"x={x}: f(x)={x}, phase={(-1) ** x}")