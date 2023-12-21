
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of a previously seen string
        for previous_string in anagram_counts:
            # If the string is an anagram of a previously seen string, increment its count
            if sorted(previous_string) == sorted(lowercase_string):
                anagram_counts[previous_string] += 1

        # Otherwise, add the new string to the dictionary and set its count to 1
        else:
            anagram_counts[lowercase_string] = 1

    # Check if there are at most 93 pairs of anagrams in the given list
    return len(anagram_counts) <= 93
