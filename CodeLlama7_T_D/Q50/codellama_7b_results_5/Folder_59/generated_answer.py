
def if_contains_anagrams(words):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(words) - 1):
        word1 = words[i]
        for j in range(i + 1, len(words)):
            word2 = words[j]
            # Check if word1 and word2 are anagrams
            if sorted(word1.lower()) == sorted(word2.lower()):
                num_pairs += 1
    return num_pairs >= 10
