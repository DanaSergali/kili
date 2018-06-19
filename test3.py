import os
import xml.etree.ElementTree as ET
from collections import Counter

def get_sentence(sentence):
    return ' '.join([x.rstrip() for x in sentence.itertext()])
    

def bigramms(filename):
    ans = ''
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
            for i in range(1, len(words)):
                anas = words[i].findall('ana')
                is_abbr = False
                abbr = ''
                for ana in anas:
                    gr = ana.get('gr')
                    if gr[0] == "S"  and gr.find('gen') != -1:
                        prev_anas = words[i - 1].findall('ana')
                        for pr_ana in prev_anas:
                            if pr_ana.get('gr')[0] == 'S':
                                ans += "{0} {1}\t{2}\n".format(pr_ana.tail, ana.tail, get_sentence(sent))
                                
    return ans


file_list = os.listdir()

main_counter = Counter()

with open('test3.txt', 'w') as file:
    for filename in file_list:
        if filename[0] == '_':
            file.write(bigramms(filename))


