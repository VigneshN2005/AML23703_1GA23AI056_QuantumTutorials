from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def superdense(message):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)                  # shared Bell pair: q0 = Alice, q1 = Bob
    qc.barrier()
    if message[1] == '1':
        qc.x(0)                  # second bit -> X
    if message[0] == '1':
        qc.z(0)                  # first bit -> Z
    qc.barrier()
    qc.cx(0, 1)                  # Bob decodes
    qc.h(0)
    qc.measure([0, 1], [1, 0])   # q0 -> c1, q1 -> c0
    return qc

qc = superdense('00')
print(qc.draw())
sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
print("Sent: 00 | Decoded counts:", counts)