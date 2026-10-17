from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()

def build_oracle(func_type):
    qc = QuantumCircuit(2)
    if func_type == "constant_0":
        pass
    elif func_type == "constant_1":
        qc.x(1)
    elif func_type == "balanced_x":
        qc.cx(0, 1)
    elif func_type == "balanced_not_x":
        qc.cx(0, 1)
        qc.x(1)
    else:
        raise ValueError("Unknown function type")
    return qc

def deutsch(func_type):
    qc = QuantumCircuit(2, 1)
    qc.x(1)
    qc.h([0, 1])
    qc.compose(build_oracle(func_type), inplace=True)
    qc.h(0)
    qc.measure(0, 0)
    counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
    return max(counts, key=counts.get)

for ft in ["constant_0", "constant_1", "balanced_x", "balanced_not_x"]:
    r = deutsch(ft)
    print(f"{ft:>15} -> measured {r} -> {'constant' if r == '0' else 'balanced'}")