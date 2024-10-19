from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def grover_algorithm(n, target):
    # Create a quantum circuit with n qubits
    qc = QuantumCircuit(n)

    # Apply Hadamard gates to all qubits
    qc.h(range(n))

    # Oracle for marking the target state
    oracle = QuantumCircuit(n)
    oracle.z(target)  # Apply Z gate to the target state
    qc += oracle

    # Apply Hadamard gates again
    qc.h(range(n))

    # Measure the qubits
    qc.measure_all()

    # Execute the circuit using the Aer simulator
    simulator = Aer.get_backend('aer_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    return counts

if __name__ == "__main__":
    n = 3  # Number of qubits
    target = 1  # Target state (binary representation)
    counts = grover_algorithm(n, target)
    print("Results of Grover's Algorithm:", counts)