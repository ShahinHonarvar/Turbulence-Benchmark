
def if_contains_anagrams(strings):
    # Initialize variables
    anagram_pairs = 0
    minimum_length = 3

    # Iterate through each string in the list
    for string in strings:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of itself
        if len(set(lowercase_string)) == len(lowercase_string):
            anagram_pairs += 1

        # Check if the string is an anagram of any other strings in the list
        for other_string in strings:
            # Convert the other string to lowercase
            lowercase_other_string = other_string.lower()

            # Check if the string and the other string are anagrams of each other
            if len(set(lowercase_string)) == len(lowercase_other_string) and sorted(lowercase_string) == sorted(lowercase_other_string):
                anagram_pairs += 1

    # Check if there are at most 21 pairs of anagrams in the list
    return anagram_pairs <= 21
