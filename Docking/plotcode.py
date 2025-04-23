import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ligands = ['Lig1', 'Lig2', 'Lig3', 'Lig4', 'Lig5']
proteins = ['Wild-Type', 'Mut1', 'Mut2', 'Mut3']
binding_energies = {
    'Lig1': [-6.8, -7.6, -7.4, -7.6],
    'Lig2': [-5.0, -5.4, -5.0, -4.6],
    'Lig3': [-8.5, -7.5, -8.4, -7.8],
    'Lig4': [-5.4, -5.0, -5.1, -4.9],
    'Lig5': [-7.2, -7.4, -7.7, -7.3]
}

# Setting up the figure for the bar graph and the density distribution plot
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.15
x = np.arange(len(proteins))

# Bar graph
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, ligand in enumerate(ligands):
    ax.bar(x + i * bar_width, binding_energies[ligand], bar_width, label=ligand, color=colors[i])

# Adding labels and title
ax.set_xlabel('Protein Variants')
ax.set_ylabel('Binding Energy (kcal/mol)')
ax.set_title('Comparative Binding Affinities of Ligands Across Protein Variants')
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(proteins)
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Invert y-axis for better presentation
ax.invert_yaxis()

# Density Distribution Graph (overlayed)
fig2, ax2 = plt.subplots(figsize=(12, 6))
for ligand in ligands:
    sns.kdeplot(binding_energies[ligand], label=ligand, shade=True, alpha=0.5)

# Adding labels and title for density plot
ax2.set_xlabel('Binding Energy (kcal/mol)')
ax2.set_ylabel('Density')
ax2.set_title('Density Distribution of Binding Energies for Each Ligand')

# Show gridlines for density plot
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

# Tight layout for both figures
plt.tight_layout()

# Save both graphs
plt.savefig('C:/Users/shubh/Semester 6/CADD/Assignment 2/binding_affinity_comparison4564545.png')

plt.show()
