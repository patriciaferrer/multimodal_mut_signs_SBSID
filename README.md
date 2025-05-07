# Multimodal mutational signatures (SBS+ID)
This repository contains the code for extracting multimodal mutational signatures (SBS + ID) as described in the method introduced in *"Joint inference of mutational signatures from indels and single-nucleotide substitutions reveals prognostic impact of DNA repair deficiencies in tumors"* by Patricia Ferrer-Torres, Iván Galván-Femenía, and Fran Supek. This study presents a multimodal method that jointly analyzes SBS and indel mutations to improve the accuracy of mutational signature extraction. We identified clinically relevant subtypes of the HR-deficiency signature SBS3 and predicted patient survival more effectively than existing approaches.

---

## **Scripts description and usage**

### 1. Obtain SBS+ID multimodal mutation count matrix

The first step is to use *SigProfilerMatrixGenerator* to generate mutation count matrices from the VCF files of multiple samples (n). This will produce two matrices:
- `SBS96` (96 x n): 96 mutation types for for single base substitutions
- `ID83` (83 x n): 83 mutation types for small insertions and deletions

To extract **multimodal mutational signatures**, both matrices are combined into a single mutation count matrix `SBS+ID` with 179 features (96 from SBS + 83 from ID), resulting in a matrix of size `179 x n`.

To join the matrices, run:

```bash
Rscript 01_join_sbs_id_matrix.R
```

### 2. Extract multimodal signatures

The combined `SBS+ID` matrix (with 179 mutation types: 96 SBS + 83 ID types) is used as input for *SigProfilerExtractor* to extract multimodal mutational signatures with NMF. The output will be a `179 × k` matrix, where `k` is the number of extracted signatures. Each signature is composed of 96 channels for SBS mutations and 83 channels for ID mutations

To run the extraction, use:

```bash
python 02_SigProfiler_Extract.py
```

### 3. Split the multimodal signature matrix

*SigProfilerExtractor* does not recognize or label SBS+ID (multimodal) signatures. Therefore, the extracted `179 × k` signature matrix must be separated into:

- SBS-only signature matrix → a `96 × k` matrix containing only the SBS portion
- ID-only signature matrix` → an `83 × k` matrix containing only the ID portion

To split the multimodal signature matrix into SBS and ID components, run:

```bash
Rscript 03_divide_SBS_ID_signatures
```

### 4. Assign COSMIC reference signatures

Once the SBS and ID signature matrices have been separated, each one can be compared to known COSMIC reference signatures using *SigProfilerAssignment*. This step identifies the likely composition of each *de novo* multimodal signature.

To perform the assignment, run:

```bash
python 04_SigProfiler_decompose_SBSID_signatures.py
```

## References

This repository uses the *SigProfiler* tool developed by Alexandrov *et al.*

Alexandrov, L.B., Kim, J., Haradhvala, N.J. et al. The repertoire of mutational signatures in human cancer. Nature 578, 94–101 (2020). https://doi.org/10.1038/s41586-020-1943-3


