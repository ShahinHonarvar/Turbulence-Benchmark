
def if_contains_anagrams(words):
    # Check if there are at least 4 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_pairs += 1
                if num_pairs >= 4:
                    return True
    return False
