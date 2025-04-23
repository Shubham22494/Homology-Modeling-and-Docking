import matplotlib.pyplot as plt
import numpy as np

# List of DOPE profile files
profile_files = ["query.profile", "mut1.profile", "mut2.profile", "mut3.profile"]
colors = ["g", "r", "b", "y"]  # Different colors for different profiles

plt.figure(figsize=(14, 6))  # Increased width and height of the figure

for file_name, color in zip(profile_files, colors):
    residues = []
    dope_scores = []
    
    try:
        with open(file_name, "r") as file:
            for line in file:
                if line.startswith("#") or not line.strip():
                    continue  # Skip comments and empty lines
                columns = line.split()
                
                try:
                    residue_index = int(columns[0])  # First column: Residue index
                    dope_score = float(columns[-1])  # Last column: DOPE score
                    
                    residues.append(residue_index)
                    dope_scores.append(dope_score)
                except (ValueError, IndexError):
                    print(f"Skipping malformed line in {file_name}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        continue
    
    # Plot the DOPE Score Profile
    plt.plot(residues, dope_scores, label=file_name, color=color, linestyle="-", markersize=2)

# Customize the plot
plt.xlabel("Residue Index")
plt.ylabel("DOPE Score")
plt.xlim(left=0, right=max(residues) + 100)  # Further extend x-axis range
plt.xticks(np.arange(0, max(residues) + 100, step=50))  # Increase x-axis scale interval
plt.title("DOPE Score Profile Comparison")
plt.axhline(y=0, color="k", linestyle="--", label="Zero DOPE Score")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save and Show Plot
plt.savefig("dope_score_comparison.png", dpi=300)
plt.show()