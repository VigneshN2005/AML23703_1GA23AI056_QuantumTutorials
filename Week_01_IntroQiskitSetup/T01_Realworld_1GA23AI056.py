import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
num_bits = 32
def generate_quantum_bits(n_bits):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulator = Aer.get_backend("aer_simulator")
    transpiled_qc = transpile(qc, simulator)
    bits = []
    for _ in range(n_bits):
        job = simulator.run(transpiled_qc, shots=1)
        result = job.result()
        bit = list(result.get_counts().keys())[0]
        bits.append(bit)
    return "".join(bits)
def generate_classical_bits(n_bits):
    return "".join(random.choice("01") for _ in range(n_bits))
def bit_balance(bit_string):
    ones = bit_string.count("1")
    return ones / len(bit_string)
quantum_bits = generate_quantum_bits(num_bits)
classical_bits = generate_classical_bits(num_bits)
print("Quantum random bits:  ", quantum_bits)
print("Classical random bits:", classical_bits)
print(f"Quantum bit balance (fraction of 1s):   {bit_balance(quantum_bits):.4f}")
print(f"Classical bit balance (fraction of 1s): {bit_balance(classical_bits):.4f}")
