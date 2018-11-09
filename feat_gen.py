#!/bin/python
from num2words import  num2words
import sys

def preprocess_corpus(train_sents):
    """Use the sentences to do whatever preprocessing you think is suitable,
    such as counts, keeping track of rare features/words to remove, matches to lexicons,
    loading files, and so on. Avoid doing any of this in token2features, since
    that will be called on every token of every sentence.

    Of course, this is an optional function.

    Note that you can also call token2features here to aggregate feature counts, etc.
    """
    for i in train_sents:
        
        for j in range(len(i)):
            i[j] = i[j].replace("\t", " ")
        for j in range(len(i)):
            i[j] = i[j].strip()

    pass

def token2features(sent, i, add_neighs = True):
    """Compute the features of a token.

    All the features are boolean, i.e. they appear or they do not. For the token,
    you have to return a set of strings that represent the features that *fire*
    for the token. See the code below.

    The token is at position i, and the rest of the sentence is provided as well.
    Try to make this efficient, since it is called on every token.

    One thing to note is that it is only called once per token, i.e. we do not call
    this function in the inner loops of training. So if your training is slow, it's
    not because of how long it's taking to run this code. That said, if your number
    of features is quite large, that will cause slowdowns for sure.

    add_neighs is a parameter that allows us to use this function itself in order to
    recursively add the same features, as computed for the neighbors. Of course, we do
    not want to recurse on the neighbors again, and then it is set to False (see code).
    """
    ftrs = []
    # bias
    ftrs.append("BIAS")
    # position features
    if i == 0:
        ftrs.append("SENT_BEGIN")
    if i == len(sent)-1:
        ftrs.append("SENT_END")

    # the word itself
    word = unicode(sent[i])
    ftrs.append("WORD=" + word)
    ftrs.append("LCASE=" + word.lower())
    # some features of the word
    if word.isalnum():
        ftrs.append("IS_ALNUM")
    if word.isnumeric():
        ftrs.append("IS_NUMERIC")
    if word.isdigit():
        ftrs.append("IS_DIGIT")
    if word.isupper():
        ftrs.append("IS_UPPER")
    if word.islower():
        ftrs.append("IS_LOWER")

    positive_emotion = { "&lt;3",":D", ":d", ":dd", ":P",":p","8)","8-)", ":-)", ":)", ";)", "(-:","(:",":')", "xD", "XD","yay!", "yay","yaay","yaaay", "yaaaay", "yaaaaay", "Yay!","Yay","Yaay","Yaaay", "Yaaaay", "Yaaaaay", "Hurray", "Hurraay", "Hurraaay"}
    negative_emotion = {":/","&gt;",":'(",":-(", ":(", ":s", ":-s", "-_-","-.-"}

    emotion = "IS_NOT_AN_EMOTION"
    if word.split(" ")[ 0 ] in positive_emotion:
        emoji = "IS_POSITIVE_EMOTION"
    elif word.split(" ")[ 0 ] in negative_emotion:
        emoji = "IS_NEGATIVE_EMOTION"
    ftrs.append(emotion)

    if word.startswith("https://") :
        if len( word[9:] )!=0:
            ftrs.append("IS_A_SECURED_URL")
        else:
            ftrs.append("IS_NOT_A_SECURED_URL")
    elif word.startswith("http://") :
        if len( word[8:] )!=0:
            ftrs.append("IS_A_URL")
        else:
            ftrs.append("IS_NOT_A_URL")


    if "!"  in word :
        ftrs.append("HAS_A_EXCLAIMATION_MARK")

    if word.startswith("@") :
        if len( word[1:] ) != 0:
            ftrs.append("IS_HEADER")
        else:
            ftrs.append("IS_NOT_HEADER")

    if "?"  in word :
        ftrs.append("HAS_A_QUESTION_MARK")

    if word.startswith("#") :
        if  len( word[1:] )!=0:
            ftrs.append("IS_A_HASHTAG")
        else:
            ftrs.append("IS_NOT_A_HASHTAG")

    w = word.split(" ")[0]

    if w.endswith("ed") :
        ftrs.append("ENDS_WITH_ED")
    elif w.endswith("ing") :
        ftrs.append("ENDS_WITH_ING")
    elif w.endswith("s") :
        ftrs.append("ENDS_WITH_S")
    elif w.endswith("es") :
        ftrs.append("ENDS_WITH_ES")
    elif w.endswith("ous") :
        ftrs.append("ENDS_WITH_OUS")

    elif w.endswith("able") :
        ftrs.append("ENDS_WITH_ABLE")
    elif w.endswith("al") :
        ftrs.append("ENDS_WITH_AL")
    elif w.endswith("an") :
        ftrs.append("ENDS_WITH_AN")
    elif w.endswith("ar") :
        ftrs.append("ENDS_WITH_AR")

    elif w.endswith("ent") :
        ftrs.append("ENDS_WITH_ENT")
    elif w.endswith("ful") :
        ftrs.append("ENDS_WITH_FUL")
    elif w.endswith("ic") :
        ftrs.append("ENDS_WITH_IC")
    elif w.endswith("ical") :
        ftrs.append("ENDS_WITH_ICAL")

    elif w.endswith("ine") :
        ftrs.append("ENDS_WITH_INE")
    elif w.endswith("ile") :
        ftrs.append("ENDS_WITH_ILE")
    elif w.endswith("ive") :
        ftrs.append("ENDS_WITH_IVE")
    elif w.endswith("less") :
        ftrs.append("ENDS_WITH_LESS")

    elif w.endswith("ous") :
        ftrs.append("ENDS_WITH_OUS")
    elif w.endswith("some") :
        ftrs.append("ENDS_WITH_SOME")
    elif w.endswith("ty") :
        ftrs.append("ENDS_WITH_TY")
    elif w.endswith("ly") :
        ftrs.append("ENDS_WITH_LY")

    elif w.endswith("ie") :
        ftrs.append("ENDS_WITH_IE")
    elif w.endswith("or") :
        ftrs.append("ENDS_WITH_OR")
    elif w.endswith("ance") :
        ftrs.append("ENDS_WITH_ANCE")
    elif w.endswith("ish") :
        ftrs.append("ENDS_WITH_ISH")

    elif w.endswith("ion") :
        ftrs.append("ENDS_WITH_ION")
    elif w.endswith("ce") :
        ftrs.append("ENDS_WITH_CE")
    elif w.endswith("ge") :
        ftrs.append("ENDS_WITH_GE")
    elif w.endswith("ite") :
        ftrs.append("ENDS_WITH_ITE")

    elif w.endswith("acy") :
        ftrs.append("ENDS_WITH_ACY")
    elif w.endswith("asy") :
        ftrs.append("ENDS_WITH_ASY")
    elif w.endswith("ize") :
        ftrs.append("ENDS_WITH_IZE")

    elif w.endswith("ise") :
        ftrs.append("ENDS_WITH_ISE")
    elif w.endswith("yze") :
        ftrs.append("ENDS_WITH_YZE")
    elif w.endswith("yse") :
        ftrs.append("ENDS_WITH_YSE")
    elif w.endswith("ance") :
        ftrs.append("ENDS_WITH_ANCE")

    elif w.endswith("ence") :
        ftrs.append("ENDS_WITH_ENCE")
    elif w.endswith("ancy") :
        ftrs.append("ENDS_WITH_ANCY")
    elif w.endswith("ency") :
        ftrs.append("ENDS_WITH_ENCY")
    elif w.endswith("ant") :
        ftrs.append("ENDS_WITH_ANT")

    elif w.endswith("ent") :
        ftrs.append("ENDS_WITH_ENT")
    elif w.endswith("ary") :
        ftrs.append("ENDS_WITH_ARY")
    elif w.endswith("ery") :
        ftrs.append("ENDS_WITH_ERY")
    elif w.endswith("ory") :
        ftrs.append("ENDS_WITH_ORY")
    elif w.endswith("y") :
        ftrs.append("ENDS_WITH_Y")

    elif w.endswith("ogue") :
        ftrs.append("ENDS_WITH_OGUE")
    elif w.endswith("og") :
        ftrs.append("ENDS_WITH_OG")
    elif w.endswith("oe") :
        ftrs.append("ENDS_WITH_OE")
    elif w.endswith("ae") :
        ftrs.append("ENDS_WITH_AE")

    elif w.endswith("ence") :
        ftrs.append("ENDS_WITH_ENCE")
    elif w.endswith("ense") :
        ftrs.append("ENDS_WITH_ENSE")
    elif w.endswith("efy") :
        ftrs.append("ENDS_WITH_EFY")
    elif w.endswith("ify") :
        ftrs.append("ENDS_WITH_IFY")
    elif w.endswith("y") :
        ftrs.append("ENDS_WITH_Y")


    ftrs.append("WORD LENGTH :"+str(len(word)-1))
    ftrs.append("HASH LENGTH :" + str(hash(word.split(" ")[0])))
    ftrs.append("BYTE LENGTH OF WORD : " + num2words(sys.getsizeof(word)).upper())

    # previous/next word feats
    if add_neighs:
        if i > 0:
            for pf in token2features(sent, i-1, add_neighs = False):
                ftrs.append("PREV_" + pf)
        if i < len(sent)-1:
            for pf in token2features(sent, i+1, add_neighs = False):
                ftrs.append("NEXT_" + pf)

    # return it!
    return ftrs

if __name__ == "__main__":
    sents = [
             [ "I PRON",
              "love ADJ",
              "and CONJ",
              ":D ADJ",
              "https://www.youtube.com/ X",
              "Yay! ADJ",
              "http://xyz.com X",
              "@abc X",
              "#xyz X"]
    ]
    preprocess_corpus(sents)
    for sent in sents:
        for i in xrange(len(sent)):
            print sent[i], ":", token2features(sent, i)
