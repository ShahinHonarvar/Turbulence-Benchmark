
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the input strings
    for string in strings:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of itself
        if lowercase_string == string:
            continue

        # Check if the string is an anagram of any other string in the input list
        for other_string in strings:
            # Convert the other string to lowercase
            lowercase_other_string = other_string.lower()

            # If the two strings are anagrams of each other, increment the anagram count
            if lowercase_string == lowercase_other_string:
                if lowercase_string in anagram_counts:
                    anagram_counts[lowercase_string] += 1

                else:
                    anagram_counts[lowercase_string] = 1

    # Check if there are at least 86 pairs of anagrams in the input list
    for string, count in anagram_counts.items():
        if count >= 2:
            return True

    return False
