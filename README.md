# Multimodal mutational signatures (SBS+ID)
This repository contains the code for extracting multimodal mutational signatures (SBS + ID) as described in the method introduced in *"Joint inference of mutational signatures from indels and single-nucleotide substitutions reveals prognostic impact of DNA repair deficiencies in tumors"* by Patricia Ferrer-Torres, Iván Galván-Femenía, and Fran Supek. This study presents a multimodal method that jointly analyzes SBS and indel mutations to improve the accuracy of mutational signature extraction. We identified clinically relevant subtypes of the HR-deficiency signature SBS3 and predicted patient survival more effectively than existing approaches.

---

### **Script description and usage**

#### 1. Extract SBS and ID mutation count matrices and join in a multimodal matrix

The first step is to use *SigProfilerMatrixGenerator* to generate mutation count matrices from the VCF files of multiple samples. This will produce two matrices:
- `SBS96` (n × 96): for single base substitutions
- `ID83` (n × 83): for small insertions and deletions

To extract **multimodal mutational signatures**, both matrices are combined into a single mutation count matrix `SBS+ID` with 179 features (96 from SBS + 83 from ID), resulting in a matrix of size `n × 179`.

To join the matrices, run:

```bash
Rscript 01_join_sbs_id_matrix
