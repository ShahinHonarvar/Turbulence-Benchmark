
def if_contains_anagrams(string_list):
    # Count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if sorted(string_list[i]) == sorted(string_list[j]):
                pair_count += 1
    # Return true if there are at least 209 anagram pairs in the list
    return pair_count >= 209
