import codecs
import nltk
from nltk.tokenize import sent_tokenize ,word_tokenize,wordpunct_tokenize
import re


def textprocess(path):
    text = codecs.open(path, 'r', 'utf-8').read()
    tokenized_text = list()
    incorrect_sent = list()
    text = re.sub(r"(\r\n)+", r"\r\n", text) # remove extra spaces
    text=re.sub(r'[^\x00-\x7F]+', ' ', text) # remove non ascii characters
    # Segment the content into sentences
    result = sent_tokenize(text)
    print("Number of sentences generated :" + str(len(result)) + "\n")
    print("incorrect sentences:")

    for n, sentence in enumerate(result):
        temp = re.compile("[A-Z]\.$|Mr\.$|St\.$")
        temp1 = re.compile("^\[")
        tokenized_text = tokenized_text + word_tokenize(sentence)
        string = u"{}".format(sentence)

        if temp.search(sentence):
            incorrect_sent.append(sentence)
            print("----" + sentence)
            incorrect_sent.append(result[n + 1])
            print(result[n + 1])
        elif temp1.search(sentence):
            incorrect_sent.append(sentence)
            print(sentence)
        # tokenized_text_punk=tokenized_text_punk+wordpunct_tokenize(sentence)

        elif re.findall(r"(?<=\r\n)+.+\r\n.+", string, re.UNICODE | re.MULTILINE):
            incorrect_sent.append(sentence)
            print(sentence)
    # print(incorrect_sent)
    print("Number of incorrect sentences generated :" + str(len(incorrect_sent)))
    print()
    print()
    print()
    # Segment the content into tokens
    # tokenized_text=word_tokenize(text)
    print("Number of words generated :" + str(len(tokenized_text)))
    print("incorrect tokens:")
    incorrect_word = list()
    # print(tokenized_text_punk)
    for n, x in enumerate(tokenized_text):
        special_char = re.compile("^'[\w]{2,}")
        special_char1 = re.compile("/|[\w]\.$")
        special_char2 = re.compile("^\[")
        special_char3 = re.compile("^'s$")
        special_char4 = re.compile("^\.$")
        # CHECK START OF single quotes
        if (special_char.search(x) != None) or (special_char1.search(x) != None):
            print(x)
            incorrect_word.append(x)
        # CHECK citation
        if special_char2.search(x):
            if tokenized_text[n + 1].isnumeric():
                print(x, tokenized_text[n + 1], tokenized_text[n + 2])
                incorrect_word.append(x)
                incorrect_word.append(tokenized_text[n + 1])
                incorrect_word.append(tokenized_text[n + 2])
        # check 's
        if special_char3.search(x):
            print(tokenized_text[n - 1], x)
            incorrect_word.append(x)
            incorrect_word.append(tokenized_text[n - 1])
        # CHECK acronym
        if special_char4.search(x):
            if tokenized_text[n - 1].isupper():
                print(tokenized_text[n - 1], x)
                incorrect_word.append(x)
                incorrect_word.append(tokenized_text[n - 1])
    print("Number of incorrect words generated :" + str(len(incorrect_word)))


#read text file





