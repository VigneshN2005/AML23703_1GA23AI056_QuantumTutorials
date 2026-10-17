from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def superdense(message):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()
    if message[1] == '1':
        qc.x(0)
    if message[0] == '1':
        qc.z(0)
    qc.barrier()
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [1, 0])
    return qc

sim = AerSimulator()
print(f"{'Sent':>5} | {'Counts':>16} | Decoded | Correct")
for msg in ["00", "01", "10", "11"]:
    counts = sim.run(transpile(superdense(msg), sim), shots=1024).result().get_counts()
    decoded = max(counts, key=counts.get)
    print(f"{msg:>5} | {str(counts):>16} | {decoded:>7} | {decoded == msg}")