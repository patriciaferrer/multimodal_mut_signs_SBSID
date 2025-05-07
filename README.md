# multimodal_mut_signs_SBSID
This repository contains the code for extracting multimodal mutational signatures (SBS + ID) as described in the method introduced in *"Joint inference of mutational signatures from indels and single-nucleotide substitutions reveals prognostic impact of DNA repair deficiencies in tumors"* by Patricia Ferrer-Torres, Iván Galván-Femenía, and Fran Supek.

---

### **Script descriptions:**

- `01_preprocessing.R`:  
  Takes raw VCF files as input and performs initial processing such as cleaning, annotation, and formatting required for downstream analysis.

- `02_feature_extraction.R`:  
  Extracts relevant features from each sample, including mutation type, sequence context, and possibly structural/genomic annotations.

- `03_modeling_signatures.R`:  
  Applies modeling techniques (e.g., matrix factorization or machine learning) to infer multimodal mutational signatures from the extracted features.

- `04_visualization.R`:  
  Creates summary plots of the learned signatures, such as barplots, heatmaps, or dimensionality reduction plots for interpretation.

---

### Usage

Run each script in sequence:

```bash
Rscript 01_preprocessing.R --input path/to/vcfs --output preprocessed_data/
Rscript 02_feature_extraction.R --input preprocessed_data/ --output features/
Rscript 03_modeling_signatures.R --input features/ --output signatures/
Rscript 04_visualization.R --input signatures/ --output plots/
