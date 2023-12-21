
def if_contains_anagrams(strings):
    # Initialize variables
    anagram_count = 0
    minimum_string_length = 3

    # Iterate over the list of strings and count the number of anagrams
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            # Check if the two strings are anagrams
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_count += 1
                break

    # Return True if there are at least 10 pairs of anagrams, False otherwise
    return anagram_count >= 10
