
def if_contains_anagrams(words):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                anagram_pairs += 1
                if anagram_pairs > 94:
                    return False

    return True
