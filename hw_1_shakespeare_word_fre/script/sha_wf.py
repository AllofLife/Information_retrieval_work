# Module that is responsible for analyzing and getting statistical results from shakespeare.txt file
# about letter frequency, total number of words, number of unique words and five most common words
# along with the words that most commonly follow them

import sys
import re
import os.path
from collections import Counter


def main():
    if len(sys.argv[1:]) >= 1:
        if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]) :
            with open(sys.argv[2], "r", encoding="utf8") as stop_file:
                stop_words_file = stop_file.read()
                stop_words_doc = stop_words_file.replace('\n',' ')
                stop_words_list = stop_words_doc.split(" ")
                print(" stop_words_list ",stop_words_list)
                print(" stop_words_list length ",len(stop_words_list))
                # print(stop_words_doc)
            with open(sys.argv[1], "r", encoding="utf8") as file:
                print("\nprogress")
                doc = data_processing(file,stop_words_list)
            letter_frequency(doc)
            print("\n")
            number_of_words(doc)
            print("\n")
            number_of_unique_words(doc)
            print("\n")
            common_words(doc)
        else:
            print("The file does not exist!")
            sys.exit(1)
    else:
        print("No argument provided. Please provide at least the shakespeare.txt and stop_words.txt ")
        print("use: python3 sha_wf.py ../data/shakespeare.txt ../data/stop_words.txt ")
        sys.exit(1)


def output_log(line):
    print(line)
    if len(sys.argv[1:]) == 3:
        with open(sys.argv[3], "a", encoding="utf8") as output:
            output.write(line + "\n")


# The idea is to replace everything that we don't need with a space character
# and finally replace all spaces created with a simple space to get the words
#  处理停用词
def data_processing(file,stop_words_list):
    shakespeare = file.read()
    # print(shakespeare)
    # 替换换行位空格
    doc = shakespeare.replace('\n', ' ')
    # 开始处理停用词
    doc = re.sub(r"\d", " ", doc)  # remove all digits
    doc = re.sub(r"[^\w\s]", " ", doc)  # remove punctuations

    doc = re.sub(r"[_]", " ", doc)  # remove special character
    doc = re.sub(r"\sd\s", " ", doc)  # remove d from words (because of 'd words)
    doc = re.sub(r"\ss\s", " ", doc)  # remove s from words (because of 's words)
    doc = re.sub(r"\so\s", " ", doc)  # remove o from words (because of 'o words)

    doc = re.sub(r"the", " ", doc)  # remove o from words (because of 'o words)
    for i in range(0,len(stop_words_list)):
        # print(i,stop_words_list[i])
        # print(stop_words_list[47])
        doc = re.sub(stop_words_list[i], " ", doc)  # remove stop words
    # doc = re.sub(stop_words_list[47], " ", doc)  # remove stop words

        

    doc = re.sub(r"\s+", " ", doc)  # substitute all spaces with a single space
    doc = doc.lower()  # lowercase every word
    doc = doc.strip()
    return doc

# 
def letter_frequency(doc):
    doc2 = tuple(re.sub(r'\s+', "", doc))
    c = Counter(doc2)
    title = "Frequency table for alphabetic letters:"
    output_log(title)
    for letter in c.most_common():
        content = f"{letter[0]} ({letter[1]} occurrences)"
        output_log(content)


def number_of_words(doc):
    words = doc.split()
    c = Counter(words)
    content = f"The total number of words is {sum(c.values())}"
    output_log(content)


def number_of_unique_words(doc):
    words = doc.split()
    c = Counter(words)
    content = f"The number of unique words is {len(c)}"
    output_log(content)


def common_words(doc):
    words = doc.split()
    c = Counter(words)
    five_most_common = dict(c.most_common(5))
    title = "The five most common words are: "
    output_log(title)
    for key, value in five_most_common.items():
        rx = r'%s (\w+){1}' % key
        prog = re.compile(rx)
        c2 = Counter(prog.findall(doc))
        three_most_common = dict(c2.most_common(3))
        content = f"{key} ({value} occurrences)"
        output_log(content)
        for key2, value2 in three_most_common.items():
            content2 = f"-- {key2}, {value2}"
            output_log(content2)


if __name__ == '__main__':
    print("\d")
    main()