
def if_contains_anagrams(strings):
    # Check that the input is a list of strings
    if not all(isinstance(s, str) for s in strings)):
        raise ValueError("Input must be a list of strings")
    # Create a dictionary to store the anagram counts
    anagram_counts = {}
    # Iterate over the input strings and count the number of anagrams
    for string in strings:
        # Convert the string to lowercase and sort it
        sorted_string = "".join(sorted(string.lower()))
        # If the sorted string is already in the dictionary, increment the count
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        # Otherwise, add a new entry to the dictionary with a count of 1
        else:
            anagram_counts[sorted_string] = 1
    # Check if there are at least 29 pairs of anagrams in the input list
    return any(count >= 29 for count in anagram_counts.values())
