import sys
import os

# Define the range of k values to loop through 
ks = [2, 3, 4, 5]

# Working directory where the mutational signatures are stored
wd_path = "path_to_folder/multimodal_SBSID_signatures/CH179/All_Solutions/"

# Loop over each value of k
for k in ks:
    # Define the paths for the SBS and ID signature files for the current k
    signatures_sbs = wd_path + "CH179_" + str(k) + "_Signatures/Signatures/CH179_S" + str(k) + "_Signatures_SBS.txt"
    signatures_id = wd_path + "CH179_" + str(k) + "_Signatures/Signatures/CH179_S" + str(k) + "_Signatures_ID.txt"
    
    # Define the paths for the sample data files (mutation count matrices)
    samples_sbs = "path_to_folder/output/SBS/X.SBS96.all"  # Replace with actual file path 
    samples_id = "path_to_folder/output/ID/X.ID83.all"    # Replace with actual file path
    
    # Define the output paths where the decomposed results will be saved
    output_sbs = "path_to_folder/multimodal_SBSID_signatures/decompose_SBS_" + str(k)
    output_id = "path_to_folder/multimodal_SBSID_signatures/decompose_ID_" + str(k)

    from SigProfilerAssignment import Analyzer as Analyze
    
    # Run the decompose_fit function for SBS96 signatures using SigProfilerAssignment
    Analyze.decompose_fit(samples_sbs, output_sbs, signatures_sbs, genome_build="GRCh37")
    
    # Run the decompose_fit function for ID83 signatures using SigProfilerAssignment
    Analyze.decompose_fit(samples_id, output_id, signatures_id, genome_build="GRCh37")
