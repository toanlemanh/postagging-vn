import py_vncorenlp
from helpers.check_models import check_models
from helpers.handle_postag import process_postag as process_word_postag


# Example usage
file_path = "./VNCoreNLP-1.2.jar"
dir_path = "./models"


# Example usage
input_file = "./output/output_corpus.txt"  
output_file = './output/pre_output.txt' 
postag_output_file = './output/final_output.txt'

if ( not check_models(file_path, dir_path) ) :
    py_vncorenlp.download_model(save_dir='./')

# Load VnCoreNLP from the local working folder that contains both `VnCoreNLP-1.2.jar` and `models` 
model = py_vncorenlp.VnCoreNLP(annotators=["wseg", "pos"], save_dir='./')
# Equivalent to: model = py_vncorenlp.VnCoreNLP(, "ner", "parse"], save_dir='/absolute/path/to/vncorenlp')

# Annotate a raw corpus
# output/output_corpus.txt as input.txt (after reading corpus)
model.annotate_file(input_file= input_file, output_file= output_file)

process_word_postag(output_file, postag_output_file)
#final output sample: 
# word1 word2 word3
# postag1 postag2 postag3
