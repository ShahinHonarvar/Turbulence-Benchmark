
def if_contains_anagrams(string_list):
    # Check if there are at least 81 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(string_list)):
        string1 = string_list[i]
        for j in range(i + 1, len(string_list)):
            string2 = string_list[j]
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                num_pairs += 1
    return num_pairs >= 81
