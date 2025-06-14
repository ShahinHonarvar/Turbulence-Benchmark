
def if_contains_anagrams(list_of_strings):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(list_of_strings)):
        str1 = list_of_strings[i]
        for j in range(i + 1, len(list_of_strings)):
            str2 = list_of_strings[j]
            if sorted(str1.lower()) == sorted(str2.lower()):
                num_pairs += 1
    # Check if there are at least 74 pairs of anagrams in the list
    return num_pairs >= 74
