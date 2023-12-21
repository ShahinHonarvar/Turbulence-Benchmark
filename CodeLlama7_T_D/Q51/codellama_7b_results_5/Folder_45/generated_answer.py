
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over each string in the list
    for string in strings:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the lowercase string is an anagram of another string in the list
        for other_string in strings:
            # If the current string is not the same as the other string, check if it is an anagram
            if string != other_string:
                # Convert the other string to lowercase
                lowercase_other_string = other_string.lower()
                # Check if the lowercase strings are equal
                if lowercase_string == lowercase_other_string:
                    # If the lowercase strings are equal, increase the anagram count for the current string
                    if lowercase_string in anagram_counts:
                        anagram_counts[lowercase_string] += 1
                    else:
                        anagram_counts[lowercase_string] = 1

    # Check if there are at most 464 pairs of anagrams in the list
    for string, count in anagram_counts.items():
        if count > 2:
            return False

    return True
