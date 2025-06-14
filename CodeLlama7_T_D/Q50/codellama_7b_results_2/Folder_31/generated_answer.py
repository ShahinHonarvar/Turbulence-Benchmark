
def if_contains_anagrams(my_list):
    # Count the number of pairs of anagrams in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_pairs += 1
    # Return true if there are at least 68 pairs of anagrams in the list; otherwise, return false.
    if anagram_pairs >= 68:
        return True
    else:
        return False
