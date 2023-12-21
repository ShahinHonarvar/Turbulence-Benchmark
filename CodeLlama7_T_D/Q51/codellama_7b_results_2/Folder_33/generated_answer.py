
def if_contains_anagrams(words):
    # Count the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Check if the two words are anagrams of each other
            if sorted(words[i]) == sorted(words[j]):
                num_pairs += 1
    # Return whether there are at most 85 pairs of anagrams in the list
    return num_pairs <= 85
