
def if_contains_anagrams(strings):
    # check if there are at least 6 pairs of anagrams in the list
    num_anagrams = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_anagrams += 1
                if num_anagrams >= 6:
                    return True
    return False
