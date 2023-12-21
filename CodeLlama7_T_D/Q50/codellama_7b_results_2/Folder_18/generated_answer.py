
def if_contains_anagrams(words):
    # Check if there are at least 106 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i + 1, len(words)):
            word2 = words[j]
            if sorted(word1) == sorted(word2):
                num_pairs += 1
    return num_pairs >= 106
