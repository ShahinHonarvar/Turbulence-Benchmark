
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1)):
        # Get the first string and sort its characters
        s1 = my_list[i]
        sorted_chars_s1 = "".join(sorted(s1))
        # Compare the sorted characters of each string in the list
        for j in range(i + 1, len(my_list)):
            s2 = my_list[j]
            sorted_chars_s2 = "".join(sorted(s2))
            if sorted_chars_s1 == sorted_chars_s2:
                anagram_pairs += 1
    # Return true if there are at most 14 pairs of anagrams in the given list; otherwise, it should return false.
    if anagram_pairs > 14:
        return False

    else:

        return True
