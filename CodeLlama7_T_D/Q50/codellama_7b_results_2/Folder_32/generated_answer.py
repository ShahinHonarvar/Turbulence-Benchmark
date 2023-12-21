
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over each string in the list
    for string in strings:
        # If the string length is less than three, skip it
        if len(string) < 3:
            continue

        # Create a lowercase version of the string
        lowercase_string = string.lower()

        # If the anagram count for this string is not in the dictionary, add it with a count of one
        if lowercase_string not in anagram_counts:
            anagram_counts[lowercase_string] = 1

        # Otherwise, increment the count for this string
        else:
            anagram_counts[lowercase_string] += 1

    # Return true if there are at least 194 pairs of anagrams in the dictionary; otherwise, return false
    return sum(anagram_counts.values()) >= 194
