
def if_contains_anagrams(words):
    # Check if there are at most 210 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i + 1, len(words)):
            word2 = words[j]
            if sorted(word1.lower()) == sorted(word2.lower()):
                num_pairs += 1
                if num_pairs > 210:
                    return False
    return True
