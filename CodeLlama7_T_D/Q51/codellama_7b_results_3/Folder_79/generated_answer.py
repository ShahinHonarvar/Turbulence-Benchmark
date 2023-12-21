
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    at_least_three_length = False
    case_insensitive_comparison = True

    # Loop through the list and count the number of anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_count += 1

    # Check if there are at most 173 pairs of anagrams
    if anagram_count <= 173:
        return True
    else:
        return False
