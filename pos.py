import codecs
import re
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, RegexpParser


def pos(path):
    text = codecs.open(path, 'r', 'utf-8').read()
    file = codecs.open("Nouns.txt", "w", "utf-8")
    file1 = codecs.open("Verbs.txt", "w", "utf-8")
    file2 = codecs.open("Nounphrases.txt", "w", "utf-8")
    result = sent_tokenize(text)
    tokenized_text = list()
    tagged_tokken = list()
    # tokkenization
    for n, sentence in enumerate(result):
        tokenized_text = tokenized_text + pos_tag(word_tokenize(sentence))
    # pos tagging
    count = 0
    for x in tokenized_text:
        if re.match(r"^N", x[1]):
            file.write(str(x[0]) + " " + str(x[1]) + "\r\n")
            count = count + 1
    print("Number of Nouns: " + str(count))
    count = 0
    for x in tokenized_text:
        if re.match(r"^V", x[1]):
            file1.write(str(x[0]) + " " + str(x[1]) + "\r\n")
            count = count + 1
    print("Number of verbs: " + str(count))
    grammar = ('''
    NP: {<DT>?<JJ>*<NN>}
        {<NNP>+} #proper noun
        {<PDT><NN>} # pre-determiners
    ''')
    chunkParser = RegexpParser(grammar)
    tree = chunkParser.parse(tokenized_text)
    count = 0
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            if subtree.label() == 'NP':
                file2.write(str(subtree) + "\r\n")
                count = count + 1
    print("Number of Nouns Phrase : " + str(count))
    file.close()
    file1.close()
    file2.close()



