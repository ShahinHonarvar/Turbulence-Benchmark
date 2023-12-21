
def if_contains_anagrams(my_list):
    # Check if there are at least 86 pairs of anagrams in the list
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_pairs += 1
                if anagram_pairs >= 86:
                    return True

    # If there are not at least 86 pairs of anagrams in the list, return False

    return False
