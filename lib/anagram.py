# anagram.py

class Anagram:
    def __init__(self, word):
        # Store the word in a normalized form (sorted letters)
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, word_list):
        # Initialize an empty list to hold the matches
        matches = []
        
        # Iterate through each word in the word list
        for word in word_list:
            # If the sorted letters of the word match the sorted letters of the initialized word,
            # add the word to the matches list
            if sorted(word.lower()) == self.sorted_word:
                matches.append(word)
        
        return matches
