import numpy as np
import matplotlib.pyplot as plt

def read_dope_profile(file_path):
    residue_indices = []
    dope_scores = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue  # Skip comments and empty lines
            parts = line.split()
            residue_indices.append(int(parts[0]))  # Residue index
            dope_scores.append(float(parts[1]))  # DOPE score
    
    return np.array(residue_indices), np.array(dope_scores)

def plot_dope_score(file_path):
    residue_indices, dope_scores = read_dope_profile(file_path)
    
    plt.figure(figsize=(10, 5))
    plt.plot(residue_indices, dope_scores, marker='o', linestyle='-', color='b', markersize=4)
    plt.xlabel("Residue Index")
    plt.ylabel("DOPE Score")
    plt.title("DOPE Score vs Residue Index")
    plt.grid(True)
    plt.show()

# Example usage
file_path = r"C:\Users\shubh\Semester 6\CADD\Assignment 1\mut1.profile"  
plot_dope_score(file_path)
