
def if_contains_anagrams(words):
    # Check if there are at least 70 pairs of anagrams in the list
    num_anagrams = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_anagrams += 1
    return num_anagrams >= 70
