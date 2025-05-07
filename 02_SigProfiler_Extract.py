import sys

# Replace with maximum number of signatures to extract
k = int(30)

# Replace 'path_to_folder' with the actual path to your folder
input_path =  "path_to_folder/output/X.SBS96_ID83.all"
output_path = "path_to_folder/multimodal_SBSID_signatures"

from SigProfilerExtractor import sigpro as sig
def main_function():    
      sig.sigProfilerExtractor(input_type="matrix", output=output_path, input_data=input_path, 
      opportunity_genome="GRCh37", minimum_signatures=1, maximum_signatures=k, nmf_replicates=100, batch_size=1, cpu=4, gpu=False)

if __name__=="__main__":
   main_function()
   
