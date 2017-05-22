import collections
import re
import sys
import ipdb
#words = re.findall(r'\w+', open('test.txt').read().lower())
#print(collections.Counter(words).most_common(2))

def load_data(filepath):
    with open(filepath, "r") as textfile:
        text = textfile.read()
    return text

def get_most_frequent_words(text):
    words = re.findall(text.lower)
    count = collections.Counter(words).most_common(10)
    return count 


if __name__ == '__main__':
    filepath = sys.argv[1]
    load_data(filepath)
    get_most_frequent_words(text)
    print(count)

  
