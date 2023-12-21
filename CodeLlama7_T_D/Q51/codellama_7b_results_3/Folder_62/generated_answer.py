
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in strings:
        # Lowercase the string and sort its characters
        sorted_string = "".join(sorted(string.lower()))

        # If the sorted string is already in the dictionary, increment its count
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1

        # Otherwise, add it to the dictionary and set its count to 1
        else:
            anagram_counts[sorted_string] = 1

    # Loop through each key in the dictionary (which is the sorted string)
    for key in anagram_counts.keys():
        # If the count for that key is greater than 289, return false
        if anagram_counts[key] > 289:
            return False

    # If none of the counts exceed 289, return true
    return True
