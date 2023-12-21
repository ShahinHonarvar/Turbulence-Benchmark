
def if_contains_anagrams(lst):
    # Initialize anagram dictionary with counts for each letter
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        letters = set(word)
        for letter in letters:
            if letter not in anagram_dict:
                anagram_dict[letter] = 1
            else:
                anagram_dict[letter] += 1
    # Check if there are at most 277 pairs of anagrams
    num_pairs = 0
    for letter, count in anagram_dict.items():
        num_pairs += (count * (count - 1)) // 2
    return num_pairs <= 277
