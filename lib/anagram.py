class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        word_sorted = sorted(self.word.lower())
        return [
            candidate for candidate in possible_anagrams
            if sorted(candidate.lower()) == word_sorted and candidate.lower() != self.word.lower()
        ]
