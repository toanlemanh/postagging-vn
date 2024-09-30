# path: src/pos/vn/helpers

def process_postag(input_file, output_file):
    words = []
    postags = []

    # Open the input file and process each line
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 2:  # Ensure the line contains at least word and POS tag
                words.append(parts[1])  # Word is in the second column
                postags.append(parts[2])  # POS tag is in the third column

    # Open the output file and write the new structure
    with open(output_file, 'w') as file:
        file.write(' '.join(words) + '\n')  # Write all words on the first line
        file.write(' '.join(postags) + '\n')  # Write all POS tags on the second line


