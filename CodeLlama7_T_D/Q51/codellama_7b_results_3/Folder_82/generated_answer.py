
def if_contains_anagrams(strings):
    # Convert all strings to lowercase
    lowercase_strings = [string.lower() for string in strings]
    # Create a set of all unique anagram pairs
    anagram_pairs = set()
    # Iterate over the list of strings
    for string1 in lowercase_strings:
        # Iterate over the list of strings again
        for string2 in lowercase_strings:
            # If the strings are not the same and have at least three letters, check if they are anagrams
            if string1 != string2 and len(string1) >= 3:
                # Check if the strings are anagrams using sorted()
                if sorted(string1) == sorted(string2):
                    # Add the pair of anagrams to the set of unique pairs
                    anagram_pairs.add((string1, string2))
    # If there are more than 40 pairs of anagrams in the list, return false
    if len(anagram_pairs) > 40:
        return False

    # Otherwise, return true

    return True
