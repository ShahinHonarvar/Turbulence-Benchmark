
def if_contains_anagrams(string_list):
    # Initialize an empty dictionary to store the counts of each string
    string_counts = {}

    # Iterate over the list of strings and count the frequency of each string
    for string in string_list:
        normalized_string = ''.join(sorted(string.lower()))

        # If the string is already in the dictionary, increase its count by 1
        if normalized_string in string_counts:
            string_counts[normalized_string] += 1

        # Otherwise, add the string to the dictionary and set its count to 1
        else:
            string_counts[normalized_string] = 1

    # Iterate over the dictionary of string counts and find the pairs of anagrams
    for string, count in string_counts.items():
        if count >= 3:
            normalized_anagram = ''.join(sorted(string)))
            for other_string, other_count in string_counts.items():
                if other_count >= 3 and normalized_anagram != ''.join(sorted(other_string))):
                    return True

    # If no pairs of anagrams were found, return False
    return False
