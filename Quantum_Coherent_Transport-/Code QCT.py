import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

TOTAL_QUBITS = 9
TOTAL_CLASSICAL_BITS = 9

# Create the quantum circuit
qc = QuantumCircuit(TOTAL_QUBITS, TOTAL_CLASSICAL_BITS)
print("Initializing Node 1 (qubits 0,1,2) to state |101>...")
qc.x(0)  # q0 = |1>
# q1 is already |0>
qc.x(2)  # q2 = |1>

# Add a barrier to visually separate the steps
qc.barrier()

# Layer 1: CNOT(source, target)
print("Moving state from Node 1 -> Node 2...")
qc.cx(0, 3)
qc.cx(1, 4)
qc.cx(2, 5)

# Layer 2: CNOT(target, source)
qc.cx(3, 0)
qc.cx(4, 1)
qc.cx(5, 2)
qc.barrier()

# Layer 3: CNOT(source, target)
print("Moving state from Node 2 -> Node 3...")
qc.cx(3, 6)
qc.cx(4, 7)
qc.cx(5, 8)

# Layer 4: CNOT(target, source)
qc.cx(6, 3)
qc.cx(7, 4)
qc.cx(8, 5)
qc.barrier()

# Measure all qubits to see the final state.
print("Measuring all qubits...")
qc.measure(range(TOTAL_QUBITS), range(TOTAL_CLASSICAL_BITS))

# Draw and save the circuit
print("Saving circuit diagram to 'circuit.png'...")
circuit_image = qc.draw(output='mpl', style='iqx')
circuit_image.savefig('circuit.png')
print("Circuit diagram saved.")

# Let's run it on a perfect simulator to check the result.
print("Running simulation...")
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("\n--- SIMULATION RESULTS ---")
print(f"Final counts: {counts}")

# The simulator should return {'101000000': 1024}
print("\nExpected result: {'101000000': 1024}")
if '101000000' in counts and counts['101000000'] == 1024:
    print("SUCCESS: The quantum state was transported correctly!")
else:
    print("FAILURE: The state was not transported as expected.")

# Save the histogram of results
histogram_image = plot_histogram(counts)
histogram_image.savefig('histogram.png')
print("Result histogram saved to 'histogram.png'.")