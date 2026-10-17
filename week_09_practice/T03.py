import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()
rounds = 20
alice_key, bob_key = "", ""

print(f"{'Round':>5} | A basis | B basis | A bit | B bit | Kept")
for r in range(rounds):
    a_basis = random.choice("ZX")
    b_basis = random.choice("ZX")
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)              # shared Bell pair
    if a_basis == "X":
        qc.h(0)
    if b_basis == "X":
        qc.h(1)
    qc.measure([0, 1], [0, 1])
    res = list(sim.run(transpile(qc, sim), shots=1).result().get_counts().keys())[0]
    b_bit, a_bit = res[0], res[1]
    kept = a_basis == b_basis
    if kept:
        alice_key += a_bit
        bob_key += b_bit
    print(f"{r + 1:>5} | {a_basis:>7} | {b_basis:>7} | {a_bit:>5} | {b_bit:>5} | {kept}")

print("\nAlice key:", alice_key)
print("Bob key:  ", bob_key)
print("Keys match:", alice_key == bob_key)