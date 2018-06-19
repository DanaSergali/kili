import os
import xml.etree.ElementTree as ET
from collections import Counter

def count_abbr(filename):
    counter = Counter()
    with open(filename, 'r', encoding='windows-1251') as file:
        root = ET.fromstring(file.read())
        body = root.find('body')
        pars = body.findall('p')
        if pars:
            sentences = []
            for par in pars:
                sentences += par.findall('se')
        else:
            sentences = body.findall('se')
        for sent in sentences:
            words = sent.findall('w')
            for word in words:
                anas = word.findall('ana')
                is_abbr = False
                abbr = ''
                for ana in anas:
                    lex = ana.get('lex')
                    if lex.isupper() and len(lex) > 1:
                        is_abbr = True
                        abbr = lex
                if is_abbr:
                    counter[abbr] += 1
    return counter


file_list = os.listdir()

main_counter = Counter()

for filename in file_list:
    if filename[0] == '_':
        counter = count_abbr(filename)
        main_counter += counter

for k, v in main_counter.most_common():
    print('{0}\t{1}'.format(k, v))

