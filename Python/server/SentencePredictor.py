import numpy as np
import sys

class SentencePredictor:

    def __init__(self, textFileName = 'speeches.txt'):
        self.manuscript = open(textFileName, encoding='utf8').read()
        self.corpus = self.manuscript.split()
        self.word_dict = {}
        self.p_dict = {}
        self.total_phrase_count = 0
        self.vocab = 0

        # Instatiate the generator
        self.pairs = self.make_pairs()
        self.computePhraseProbability()

    # Probably done wrong - Need a 1d array to match input size
    # Probabilities in a p-dist array must sum to 1.0
    def generate_probability_distribution(self, size):
        p = []
        highestChance = 0.5
        for i in range(size - 1):
            p.append(highestChance)
            highestChance = highestChance / 2
        p.append(1 - sum(p))
        return p

    # Construct a generator 
    # This will yeild tuples that look like <Current Word, Next Word> 
    # We should expect this to yeild 1 tuple for every non-unique word
    def make_pairs(self):
        for i in range(len(self.corpus)-1):
            step = 0
            wordsUntilPeriod = []
            while(self.corpus[i + step][-1] != '.' ):
                wordsUntilPeriod.append(self.corpus[i + step])
                step += 1
            wordsUntilPeriod.append(self.corpus[i + step])
            wordsUntilPeriod = ' '.join(wordsUntilPeriod[1:])
            yield (self.corpus[i], wordsUntilPeriod)

    def computePhraseProbability(self):
        for word, sentenceEnd in self.pairs:
            self.total_phrase_count += 1
            if word in self.word_dict.keys():
                self.word_dict[word].append(sentenceEnd)
            else:
                self.vocab += 1
                self.word_dict[word] = [sentenceEnd]

        # Create matching p-val dicts
        for word, listOfTrailers in self.word_dict.items():
            self.p_dict[word] = self.generate_probability_distribution(len(listOfTrailers))


    def predictPhrase(self, word = None):
        isLastWordOfSentence = False
        
        if(word):
            if(word[-1] == '.'):
                isLastWordOfSentence = True
                word = word[:-1]
            first_word = word
            chain = [first_word]
            if first_word not in self.word_dict.keys():
                first_word = np.random.choice(self.corpus)
                chain = [first_word]

        else:
            first_word = np.random.choice(self.corpus)
            chain = [first_word]

        sentence_end = np.random.choice(self.word_dict[chain[-1]], p = self.p_dict[chain[-1]])
       
        # String together with spaces
        finalChain = ''.join(sentence_end)
        if( isLastWordOfSentence ):
            finalChain = ' ' + finalChain
        return finalChain

def beginConsoleApp():
    running = True
    user_input = ""
    sp = SentencePredictor()
    print("start typing a sentence, then hit tab")
    while(running):
        char = sys.stdin.read(1)  # read 1 character from stdin
        if char == '\t':  # if a tab was read
            corpus = user_input.split()
            pred = sp.predictPhrase(corpus[-1])
            print(' '.join(corpus[:-1]).strip(), pred)
            corpus = []
            user_input = ""
        user_input += char

if __name__ == "__main__": 
    beginConsoleApp() 
