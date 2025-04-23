
# Computational Drug Discovery: Homology Modeling and Molecular Docking Analysis of P25942

## Overview

This repository documents a two-part computational study on the P25942 protein (CD40), covering:
1. **Homology modeling and structural analysis of wild-type and mutated protein forms.**
2. **Molecular docking of five drug candidates with these protein models to evaluate binding affinities.**

The work aims to understand how point mutations in P25942 affect structural stability and ligand binding, with the broader goal of identifying promising inhibitors relevant to neuroinflammatory and neurodegenerative pathways.

---

## Assignment 1: Homology Modeling and Structural Analysis

### Objectives
- Identify suitable templates for homology modeling.
- Introduce biologically relevant point mutations.
- Generate wild-type and mutant 3D structures.
- Assess structural impacts via DOPE scores and RMSD.
- Visualize models using UCSF Chimera.

### Mutations Introduced
| Mutation ID | Substitution | Position |
|-------------|--------------|----------|
| MUT1        | P → A        | 227      |
| MUT2        | I → V        | 208      |
| MUT3        | T → M        | 112      |

### Tools & Techniques
- **BLAST** for template selection.
- **MODELLER** for structure prediction.
- **UCSF Chimera** for visualization and analysis.
- **DOPE Score & RMSD** for structural comparison.

### Key Results
- **Most Stable Model:** Wild-type (DOPE: -17296.05)
- **Least Deviation:** MUT2 (RMSD: 0.778 Å)
- **Most Destabilizing:** MUT1 (DOPE: -16268.22)

---

## Assignment 2: Molecular Docking Analysis

### Objectives
- Select drug molecules with documented acetylcholinesterase (AChE) inhibitory activity.
- Prepare ligands and models for docking.
- Perform docking using AutoDock Vina.
- Compare binding affinities across wild-type and mutated models.

### Ligands Studied
| Ligand ID | Compound Name                             | PubChem CID  | Key Feature |
|-----------|--------------------------------------------|--------------|-------------|
| Lig1      | Bisnorcymserine                           | 11799694     | Reversible AChE inhibitor |
| Lig2      | 2-Chlorobenzyl-piperazine derivative      | 137517259    | Dual-binding site AChE inhibitor |
| Lig3      | Naphthalene-sulfonamide derivative        | 137517260    | Dual AChE/BChE inhibitor |
| Lig4      | 1H-Pyrazol-3-yl derivative A              | 137517262    | CNS-targeted inhibitor |
| Lig5      | Benzimidazole-imidazopyridine hybrid      | 137517264    | Multi-target neuroprotective agent |

### Protein Models
- **Wild-Type:** P25942.B99990001
- **Mutants:** MUT1, MUT2, MUT3

### Docking Configuration
- **Tool:** AutoDock Vina
- **Center:** (-124.154, -3.109, 68.946)
- **Size:** (58, 74, 66)
- **Output:** Binding energy in kcal/mol

### Key Findings
- **Best Ligand:** Lig3 (strongest affinity: -8.5 kcal/mol with wild-type)
- **Worst Ligand:** Lig2 (weakest binding across models)
- **Mutations Impact:**
  - MUT1 & MUT3 improved Lig1 binding
  - MUT3 weakened Lig2 affinity
  - MUT2 enhanced Lig5 binding

---

## Combined Insights

- **Mutation 1** (P → A) destabilizes protein structure but enhances Lig1 binding.
- **Mutation 2** (I → V) introduces minimal structural change and favors Lig3 and Lig5 binding.
- **Mutation 3** (T → M) is structurally stable and alters hydrogen bonding, affecting Lig2 and Lig3 interaction.

Ligand 3 shows the highest promise for further development, being robust across mutations and showing consistent high-affinity binding.

---

## Supplementary Links

- 📂 **Homology Models & Mutation Files:** [Google Drive](https://drive.google.com/drive/folders/13xx8kMsPGQvhERQ1glCA7ZJb8ERs-hoz?usp=drive_link)  
- 📂 **Docking Screenshots & Input Files:** [Google Drive](https://drive.google.com/drive/folders/1E2zOOMhxbeDZunr1DNy6WBQSzFfND37C?usp=drive_link)

---

