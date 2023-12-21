
def if_contains_anagrams(my_list):
    # initialize an empty dictionary to store the counts of each letter
    letter_counts = {}
    for word in my_list:
        # convert the word to lowercase and split it into individual letters
        word_lower = word.lower()
        letters = set(word_lower)
        # if the length of the word is at least 3, increment the count of each letter
        if len(letters) >= 3:
            for letter in letters:
                if letter not in letter_counts:
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] += 1
    
    # check if there are at most 181 pairs of anagrams in the list
    pairs = 0
    for letter, count in letter_counts.items():
        pairs += (count * (count - 1)) // 2
        if pairs > 181:
            return False
    
    return True
