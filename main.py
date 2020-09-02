# -*- coding: utf-8 -*-
import sample
import remove
import dictionary
import nltk
import re

#### INPUT STEP ####
s = input('Please input the sentence: ')    # input the sentence
if s == "sample sentence":
    s = sample.sentence
tokens = nltk.word_tokenize(s)
tokens  # word decomposition
tagged = nltk.pos_tag(tokens) # add tags to each word

#### PREPARATION STEP ####
tagged2 = remove.remover(tagged)
tagged_new = tagged2[0]
string_new = tagged2[1]
##(e.g. [('I', 'PRP'), ('play', 'VBP'), ('soccer', 'NN'), ('.', '.')]
##   => ['I', 'PRP', 'play', 'VBP', 'soccer', 'NN', '.', '.'])

## str of s1, s2
s1 = tagged_new[::2]    # s1 is the array of sentence from input (= tokens)
                        #=> ['I', 'play', 'soccer', '.']
s2 = tagged_new[1::2]   # s2 is the array of POS tagging.
                        #=> ['PRP', 'VBP', 'NN', '.']

# from dictinary.py
color_dic = dictionary.color_dic
pos_tag_dic = dictionary.pos_tag_dic

#### OUTPUT STEP ####
for i in range(len(s2)):
    if s2[i] == 'VB' or s2[i] == 'VBD' or s2[i] == 'VBG' or s2[i] == 'VBN' or s2[i] == 'VBP' or s2[i] == 'VBZ':
        print(color_dic['red']+s1[i]+color_dic['end'], end='')       # verb => red
    elif s2[i] == 'JJ' or s2[i] == 'JJR' or s2[i] == 'JJS':
        print(color_dic['blue']+s1[i]+color_dic['end'], end='')      # adj => blue
    elif s2[i] == 'RB' or s2[i] == 'RBR' or s2[i] == 'RBS':
        print(color_dic['green']+s1[i]+color_dic['end'], end='')     # adv => green
    elif s2[i] == ".":
        print(s1[i]+"\n")
    elif s2[i] == "":
        if s2[i-1] != "":
            print(",", end='')
        else: continue
    else:
        print(s1[i], end='')
    if s2[i] != "." or "" :
        print(" ", end='')
print("\n")

print("word      |POS    |Part-of-speech tagging")
print("--------------------------------------------")

n1 = 10 # n1 is to adjust width between word, and POS
n2 = 7  # n2 is to adjust width between POS, and Part-of-speech tagging
count = 0   # count is the number of sentenses

for i in range(len(tagged_new)):
    if i % 2 == 0:  # tagged_new[i] => TRUE: sentence, FAULSE: pos_tag
        print(tagged_new[i], end='')
        if len(tagged_new[i]) < n1: # adust the length 1
            for j in range(n1 - len(tagged_new[i])):
                print(" ", end='')
        print("|"+tagged_new[i+1], end='')  # output "POS"
        if len(tagged_new[i]) < n2: # adjust the length 2
            for k in range(n2 - len(tagged_new[i+1])):
                print(" ", end='')
        for l in range(len(pos_tag_dic)):
            if tagged_new[i+1] == pos_tag_dic[l]:   # output "Part-of-speech"
                print("|"+pos_tag_dic[l+1])
        if tagged_new[i] == ".":
            print("|.")
            print("--------------------------------------------")
            count = count+1

if count == 0:
    print("--------------------------------------------")
if count == 1:
    print(str(count)+" sentence", end='')
else :
    print(str(count)+" sentences", end='')
print(" (color: "+color_dic['red']+"verb"+", "+color_dic['blue']+"adjective"+color_dic['blue']+", "+color_dic['green']+"adverb"+color_dic['end']+")\n")
