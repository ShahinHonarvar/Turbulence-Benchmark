
def if_contains_anagrams(string_list):
    # Initialize variables for tracking anagram pairs
    pair_count = 0
    pair_length = 3

    # Iterate over the list of strings and compare each string to every other string
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            # Check if the two strings are anagrams
            if sorted(string_list[i]) == sorted(string_list[j]):
                pair_count += 1
                    # Check if the pair is of length at least three
                    if len(string_list[i]) >= pair_length:
                        return True
    # If no anagram pairs were found, return False
    return False
