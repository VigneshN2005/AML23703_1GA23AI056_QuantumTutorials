import qiskit
from qiskit_aer import Aer
print("Qiskit version:", qiskit.__version__)
available_backends = Aer.backends()
print("Available Aer backends:")
for backend in available_backends:
    print(" -", backend.name)
