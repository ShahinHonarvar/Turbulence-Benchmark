
def if_contains_anagrams(string_list):
    # Count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(string_list)):
        string1 = string_list[i]
        for j in range(i + 1, len(string_list)):
            string2 = string_list[j]
            # Check if the strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                pair_count += 1
                
    # Return true if there are at least 97 pairs of anagrams in the list, otherwise return false
    return pair_count >= 97
