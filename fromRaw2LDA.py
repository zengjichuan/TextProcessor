__author__ = 'zengjichuan'

import nltk
import os
import os.path
import re
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader

import sys


def load_data():
    data_folder = '/Users/zengjichuan/Dropbox/sharedDataset/text/20newsUsedInSentencReglarizerPaper'
    corpus = {}
    for root, dirs, files in os.walk(data_folder):
        for file_name in files:
            if re.match(r'\d+', file_name):
                raw = open(os.path.join(root, file_name)).read()
                corpus[file_name] = raw
    return corpus

if __name__ == '__main__':

    # files' content list
    files_content = []

    # file to write
    output_file = '/Users/zengjichuan/Dropbox/sharedDataset/text/20newsUsedInSentencReglarizerPaper/20news_LDA_text.dat'

    # load raw corpus
    my_corpus = load_data()

    # stopwords filter
    stop_words = stopwords.words('english')

    # generate words bag
    for file_raw in my_corpus:
        print 'processing ', file_raw, my_corpus[file_raw][:20]
        if file_raw == '61293':
            file_word_bag = sorted(w.lower() for w in nltk.word_tokenize(my_corpus[file_raw])
                               if w.isalpha() and w.lower() not in stop_words)
            files_content.append(' '.join(file_word_bag)+'\n')
    print 'LDA Text Token Generated!'

    # write file
    with open(output_file, 'w') as f_out:
        # write documents number
        f_out.write(str(len(files_content))+'\n')
        # write content
        f_out.writelines(files_content)

    print 'From Raw Text to LDA Text Tokens Finished!'
