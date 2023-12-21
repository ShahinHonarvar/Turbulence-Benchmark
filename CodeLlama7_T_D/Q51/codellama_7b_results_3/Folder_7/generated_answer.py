
def if_contains_anagrams(string_list):
    # Check for duplicates in the list
    if len(string_list) != len(set(string_list)):
        return False

    # Check for anagram pairs

    anagram_pairs = 0

    for i in range(len(string_list) - 1):

        for j in range(i + 1, len(string_list))):

            if sorted(string_list[i]) == sorted(string_list[j])):

                anagram_pairs += 1

    return anagram_pairs <= 445
