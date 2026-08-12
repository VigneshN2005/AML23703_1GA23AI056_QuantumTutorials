from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator

qc=QuantumCircuit(2,2)

qc.h(0)
qc.cx(0,1)

qc.measure([0,1],[0,1])

sim=AerSimulator()

job=sim.run(transpile(qc,sim),shots=1024)
result=job.result()

counts=result.get_counts()

print(counts)