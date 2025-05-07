# Load necessary libraries
library(data.table)
library(dplyr)

# Define the values of k to loop over (e.g., number of mutational signatures)
ks <- c(2:5)

# Loop over the values of k
for (k in ks) {
  
  # Construct the path to the input file containing combined SBS and ID signatures
  input_path <- paste0("path_to_folder/multimodal_SBSID_signatures/CH179/All_Solutions/CH179_", 
                       k, "_Signatures/Signatures/CH179_S", k, "_Signatures.txt")
  
  # Read combined mutational signatures (SBS + ID) file
  sbsid <- fread(input_path)
  
  # Extract SBS96 (first 96 rows) and rename columns
  sbs <- sbsid[1:96, ]
  colnames(sbs) <- gsub("CH179", "SBS96", colnames(sbs))
  
  # Extract ID83 (rows 97 to 179) and rename columns
  id <- sbsid[97:179, ]
  colnames(id) <- gsub("CH179", "ID83", colnames(id))
  
  # Define output file paths
  output_dir <- paste0("path_to_folder/multimodal_SBSID_signatures/CH179/All_Solutions/CH179_", 
                         k, "_Signatures/Signatures/")
  sbs_outfile <- paste0(output_dir, "SBS96_S", k, "_Signatures.txt")
  id_outfile  <- paste0(output_dir, "ID83_S", k, "_Signatures.txt")
  
  # Write individual SBS and ID signature files
  fwrite(sbs, sbs_outfile, sep = "\t", quote = FALSE)
  fwrite(id,  id_outfile,  sep = "\t", quote = FALSE)
}