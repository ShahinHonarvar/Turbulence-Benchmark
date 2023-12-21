
def if_contains_anagrams(words):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_pairs += 1
                if num_pairs >= 8:
                    return True
    return False
