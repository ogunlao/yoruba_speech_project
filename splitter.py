import math

MAX_SENTENCE_LEN = 20
SOURCE_PATH = 'yor_trans.txt'
DEST_TEMP_PATH = 'yor_split.txt'
NUM_FOLDER_SPLIT = 50
FOLDER_PATH="split_text"
PARTIAL_NAME= "yor_split"

def split_file(source_path, dest_path, max_sentence_len):
    f = open(source_path, 'r')
    new_f = open(dest_path, 'w')
    for line in f:
        line = line.replace('\n', '')
        splitted_text = line.split(" ")
        total_words = len(splitted_text)
        if total_words > 1:
            if total_words <= max_sentence_len:
                line = line + " ## .\n"
                new_f.write(line)
            else:
                # sentence longer than "max_sentence_len"
                num_split = math.ceil(total_words/max_sentence_len)
                for i in range(num_split):
                    cut_sentence = splitted_text[i*max_sentence_len: (i+1)*max_sentence_len]
                    cut_sentence.append("## .\n")
                    cut_sentence = " ".join(cut_sentence)
                    new_f.write(cut_sentence)
    
    f.close()
    new_f.close()
    return "done"

def split_file_into_folders(folder_path, source_path, partial_file_name, num_folder_split):
    f = open(source_path, 'r')
    count = 0
    text = ""
    for idx, line in enumerate(f):
        text = text+line
        if idx % (num_folder_split-1) == 0 and idx!=0:
            file_name = folder_path+"/"+partial_file_name+"_"+str(count)+".txt"
            with open(file_name, 'w') as new_split_f:
                new_split_f.write(text)
            text = ""
            count += 1


status = split_file(SOURCE_PATH, DEST_TEMP_PATH, MAX_SENTENCE_LEN)
if status == 'done':
    split_file_into_folders(FOLDER_PATH, DEST_TEMP_PATH, PARTIAL_NAME, NUM_FOLDER_SPLIT)

