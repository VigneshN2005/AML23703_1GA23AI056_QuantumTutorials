from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector.from_instruction(qc)
print("Bell state before measurement:")
print(state)

outcome, collapsed = state.measure([0])
print(f"\nMeasured qubit 0, outcome: {outcome}")
print("Resulting state of full system after partial measurement:")
print(collapsed)

reduced = partial_trace(collapsed, [0])
print("\nReduced density matrix of qubit 1:")
print(reduced)