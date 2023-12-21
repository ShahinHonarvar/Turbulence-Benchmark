
def if_contains_anagrams(string_list):
    # Initialize variables to keep track of anagram pairs
    anagram_pairs = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list))):
            # Check if the current strings are anagrams
            if sorted(string_list[i]) == sorted(string_list[j])):
                # Increment the number of anagram pairs found
                anagram_pairs += 1
    return anagram_pairs >= 153
