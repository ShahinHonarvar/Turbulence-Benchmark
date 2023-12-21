
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_count += 1
                # If there are more than 48 pairs of anagrams, return False
                if anagram_count > 48:
                    return False

    # If there are at most 48 pairs of anagrams in the list, return True
    return True
