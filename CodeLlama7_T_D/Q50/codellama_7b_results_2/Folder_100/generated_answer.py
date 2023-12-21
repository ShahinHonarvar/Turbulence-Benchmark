
def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        # Check if the string is at least three characters long
        if len(string) < 3:
            continue

        # Convert the string to lowercase
        string = string.lower()

        # Iterate over the other strings in the list
        for other_string in strings:
            # Skip the current string (i.e., the outer loop variable)
            if other_string == string:
                continue

            # Check if the other string is at least three characters long
            if len(other_string) < 3:
                continue

            # Convert the other string to lowercase
            other_string = other_string.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string) == sorted(other_string):
                anagram_count += 1

    # Return whether there are at least 95 pairs of anagrams in the given list
    return anagram_count >= 95
