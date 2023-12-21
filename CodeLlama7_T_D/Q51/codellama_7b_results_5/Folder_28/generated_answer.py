
def if_contains_anagrams(word_list):
    anagram_pairs = set()
    for word in word_list:
        # Convert the word to a list of lowercase letters
        word_as_list = [c.lower() for c in word]
        # Sort the list of letters
        sorted_word = "".join(sorted(word_as_list))
        # Check if there are any other words in the list that have the same sorted form as this word
        if any(sorted_word == "".join(sorted(w))) for w in word_list):
            anagram_pairs.add((word, sorted_word))
    return len(anagram_pairs) <= 78
