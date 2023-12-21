
def if_contains_anagrams(string_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    anagram_length = 3

    # Iterate through the list of strings and compare each string to every other string in the list
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            # If the two strings are anagrams of each other, increment the pair count
            if sorted(string_list[i]) == sorted(string_list[j]):
                pair_count += 1
                # If the number of anagram pairs exceeds 81, return False immediately
                if pair_count > 81:
                    return False

    # If no more than 81 anagram pairs are found in the list, return True
    return True
