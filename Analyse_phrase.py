import string
# in this file, i am going to try to create a code that analyse every thing in a sentence.


class Sentence(object):

    def __init__(self, phrase):
        self.phrase = phrase
        self.subject = []
        self.verb = []
        self.noun = []
        self.personal_pronoun = []
        self.stop_word = []
        self.punctuation = []
        self.article = []

    subject = ["i", "you", "he", "she", "it", "we", "they"]
    personal_pronoun = ["my", "your", "her", "his", "its", "our", "their"]
    stop_word = ["then", "in", "out", "of", "from", "at", "it", "there",  "here"]
    article = ["the", "a", "an"]

    def __str__(self):
        return "Subject: %s\nPersonal pronoun: %s\nStop_word: %s\nNoun: %s\nPunctuation: %s\nArticle: %s" % \
               (self.subject, self.personal_pronoun, self.stop_word, self.noun, self.punctuation, self.article)

    def check_punctuation(self, word):
        res = []
        for i in word:
            if i in string.punctuation:
                self.punctuation.append(i)
            else:
                res.append(i)

        return "".join(res)

    def checking(self):
        word = self.phrase.split()
        for i in word:

            if i.lower() in Sentence.subject:
                self.subject.append(self.check_punctuation(i))

            elif i.lower() in Sentence.personal_pronoun:
                self.personal_pronoun.append(self.check_punctuation(i))

            elif i.lower() in Sentence.stop_word:
                self.stop_word.append(self.check_punctuation(i))

            elif i.lower() in Sentence.article:
                self.article.append(self.check_punctuation(i))

            else:
                self.noun.append(self.check_punctuation(i))

        return

    # i am going to add some new features here, like counting the word that the sentence have.
    def count_word(self):
        res = []
        for i in self.phrase.split():
            res.append(self.check_punctuation(i))

        return len(res)



phrase = input("write a sentence: ")

# let's have a real phrase, a sentence that makes sense.

analyse = Sentence(phrase)

"""apply the function before you return the value you want, like here we want to get the result of checking
   you can try to print your analyse without it and see what i mean
"""

analyse.checking()
print(analyse)

# it's not in its final yet, i will try to make it better everyday


"""your_phrase = input("> ")
analyse1 = Sentence(your_phrase)
analyse1.checking()
print(analyse1)
"""
# it's so cool right?
print(analyse.count_word())

# let's deal with a file, not just a sentence.


