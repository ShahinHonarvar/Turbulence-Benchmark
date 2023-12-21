
def if_contains_anagrams(words):
    # Check if there are at least 86 pairs of anagrams in the list
    num_anagrams = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_anagrams += 1
                # If there are at least 86 pairs of anagrams, return True
                if num_anagrams >= 86:
                    return True

    # If there are less than 86 pairs of anagrams, return False
    return False
