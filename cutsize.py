import os


def split_my_file(sourcefile, outputfilepath, max_size):
    maxfile_size = os.path.getsize(sourcefile)
    if maxfile_size > max_size:
        with open(sourcefile, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            file_number = 0
            line_count = 0
            outfile = None

            for line in lines:
                if not outfile or os.path.getsize(outputfilepath) + len(line.encode('utf-8')) > max_size:
                    file_number += 1
                    outputfilepath = str(outputfilebase) + "-" + str(file_number) + '.txt'
                    outfile = open(outputfilepath, mode='w', newline='', encoding='utf-8')
                    line_count = 0

                outfile.write(line)
                line_count += 1

            if outfile:
                outfile.close()


sourcefilepath = r"C:\genereatePasswordList\noinevek-8digit.txt"  # sourcefile
outputfilebase = r"C:\genereatePasswordList\noinevek-8digit"  # path to output files
max_size = 20 * 1024 * 1024  # max filesize in MB in this example it splits up to 20 MB files.
split_my_file(sourcefilepath, outputfilebase, max_size)
