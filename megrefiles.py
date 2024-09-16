def concatenate_files(filenames, output_file):
    with open(output_file, 'w') as fo:
        for filename in filenames:
            with open(filename, 'r') as f:
                fo.write(f.read())


# Example usage:
filenames = ['An-ka-Ban-ka-4digit.txt', 'An-ka-Ban-ka-6digit.txt', 'An-ka-Ban-ka-8digit.txt']
output_file = 'Andr-Bandi-4-6-8.txt'
concatenate_files(filenames, output_file)


