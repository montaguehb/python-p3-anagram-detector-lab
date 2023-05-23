# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        return[n for n in words if sorted(list(n)) == sorted(list(self.word))]
