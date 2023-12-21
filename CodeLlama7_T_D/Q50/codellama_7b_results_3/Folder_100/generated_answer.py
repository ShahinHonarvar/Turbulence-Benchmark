
def if_contains_anagrams(string_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list)):
            if sorted(string_list[i]) == sorted(string_list[j]):
                anagram_pairs += 1
    # Check if there are at least 95 pairs of anagrams in the list
    return anagram_pairs >= 95
