
import matplotlib.pyplot as plt

def plot_results(counts):
    # Extract states and their probabilities
    states = list(counts.keys())
    probabilities = [count / sum(counts.values()) for count in counts.values()]

    # Create bar plot
    plt.bar(states, probabilities)
    plt.xlabel('States')
    plt.ylabel('Probabilities')
    plt.title('Results of Quantum Algorithm')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../docs/results_visualization.png')
    plt.show()

if __name__ == "__main__":
    from quantum_grover import grover_algorithm
    n = 3  # Number of qubits
    target = 1  # Target state (binary representation)
    counts = grover_algorithm(n, target)
    plot_results(counts)