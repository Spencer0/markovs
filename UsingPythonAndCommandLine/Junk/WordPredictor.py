import numpy as np
import sys


class StringPredictor:

    def __init__(self, textFileName = 'speeches.txt'):
        self.manuscript = open(textFileName, encoding='utf8').read()
        self.corpus = self.manuscript.split()
        self.word_dict = {}
        self.p_dict = {}
        self.total_word_count = 0
        self.vocab = 0
        # Instatiate the generator
        self.pairs = self.make_pairs()
        self.computePhraseProbability()

    # Probably done wrong - Need a 1d array to match input size
    # Probabilities must sum to 1.0
    def generate_probability_distribution(self, size):
        p = []
        bestChance = 0.5
        for i in range(size - 1):
            p.append(bestChance)
            bestChance = bestChance / 2
        p.append(1 - sum(p))
        return p

    # Construct a generator 
    # This will yeild tuples that look like <Current Word, Next Word> 
    # We should expect this to yeild 1 tuple for every non-unique word
    def make_pairs(self):
        for i in range(len(self.corpus)-1):
            yield (self.corpus[i], self.corpus[i+1])

    def computePhraseProbability(self):
        for word_1, word_2 in self.pairs:
            self.total_word_count += 1
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.vocab += 1
                self.word_dict[word_1] = [word_2]

        # Create matching p-val dicts
        for word, listOfTrailers in self.word_dict.items():
            self.p_dict[word] = self.generate_probability_distribution(len(listOfTrailers))


    def predictPhrase(self, word = None):
        if(word):
            first_word = word
            chain = [first_word]
            if first_word not in self.word_dict.keys():
                first_word = np.random.choice(self.corpus)

        else:
            first_word = np.random.choice(self.corpus)
            chain = [first_word]

        n_words = 10
        # begin chaining
        for i in range(n_words):
            new_word = np.random.choice(self.word_dict[chain[-1]], p = self.p_dict[chain[-1]])
            chain.append(new_word)
            if(new_word[-1] == '.'):
                return ' '.join(chain)
                break

        # String together with spaces
        finalChain = ' '.join(chain) + "."
        return finalChain


print("start typing a sentence, and then when you are ready for an ending, hit tab")
def beginConsoleApp():
    running = True
    user_input = ""
    sp = StringPredictor()

    while(running):
        char = sys.stdin.read(1)  # read 1 character from stdin
        if char == '\t':  # if a tab was read
            corpus = user_input.split()
            combo = ' '.join(corpus[:-1]) +' ' +  sp.predictPhrase(corpus[-1])
            print("\n", combo)
            corpus = []
            user_input = ""
        user_input += char

if __name__ == "__main__": 
    beginConsoleApp() 
