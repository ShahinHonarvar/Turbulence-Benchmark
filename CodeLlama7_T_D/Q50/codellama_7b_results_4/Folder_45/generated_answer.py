
def if_contains_anagrams(words):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(words) - 1):
        word1 = words[i]
        for j in range(i + 1, len(words)):
            word2 = words[j]
            if is_anagram(word1, word2):
                num_pairs += 1
    # Return True if there are at least 277 pairs of anagrams in the list; otherwise return False
    return num_pairs >= 277
# Check if two strings are anagrams of each other
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())
