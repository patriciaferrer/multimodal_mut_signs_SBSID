library(data.table)

# Read SBS96 mutational matrix
# Replace 'path_to_folder' with the actual path to your folder and "X" to the project name you chose
sbs <- fread("path_to_folder/output/SBS/X.SBS96.all")

# Read ID83 mutational matrix
id <- fread("path_to_folder/output/ID/X.ID83.all")

# Combine SBS and ID signature data into a single data frame
sbsid <- rbind(sbs, id)

# Check dimensions of the combined dataset
dim(sbsid)

# Save the combined SBSID mutational matrix
fwrite(sbsid, "path_to_folder/output/X.SBS96_ID83.all", quote = FALSE, sep = "\t")
