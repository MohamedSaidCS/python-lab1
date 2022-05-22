import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    exit('Must pass file as argument.')


def find_most_common_words(file):
    text = open(file, 'r').read()
    word_tuples = Counter(re.split(", | |\. |\.", text)).most_common(20)
    return list(map(lambda t: t[0], word_tuples))


def write_words_to_file(words):
    file = open('popular_words.txt', 'w')
    for word in words:
        file.write(word+'\n')
    print('Done.')


write_words_to_file(find_most_common_words(sys.argv[1]))
