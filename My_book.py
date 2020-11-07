import string


class Analyze(object):

    def __init__(self, filename):
        self.filename = filename
        self.hist = {}
        self.each_word = []

    def open_file(self):
        return open(self.filename)

    def show_content(self):
        fp = self.open_file()
        for line in fp:
            word = line.strip()
            print(word)

    def all_word(self):
        fp = self.open_file()

        for line in fp:
            sentence = line.strip()
            for word in sentence.split():
                self.each_word.append(word)

        return self.each_word

    def word_frequency(self):
        res = self.all_word()

        all_punctuation = string.punctuation + string.whitespace

        for word in res:
            # remove punctuation
            word = word.strip(all_punctuation)
            word = word.lower()

            self.hist[word] = self.hist.get(word, 0) + 1

        return self.hist

    def most_common(self):
        # in order to make them in order, we need to encapsulate everything in a list
        # let's create our list

        res = []

        for val, freq in self.hist.items():
            res.append((freq, val))

        """i actually tried to use this before but it sounds to be not correct: res.append((val, freq))
           the problem with this is that the sort() method will check the first element which is val.
           and that doesn't make sense if we want to have the most common word, right?
        """
        res.sort()
        res.reverse()

        for freq, val in res:
            space = " " * (15 - len(val))
            print(val + space + "> " + str(freq))


file = Analyze("my_file")

"""
file.open_file()
file.show_content()
file.all_word()
file.word_frequency()
file.most_common()
"""

# now we can use this as a module everytime, that is so cool right?




