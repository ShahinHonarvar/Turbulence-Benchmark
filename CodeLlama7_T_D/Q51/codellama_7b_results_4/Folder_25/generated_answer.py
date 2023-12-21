
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    anagram_set = set()
    # Iterate through the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is a valid anagram
        if len(lowercase_string) >= 3 and len(lowercase_string) <= 7:
            # Add the string to the set of anagrams
            anagram_set.add(lowercase_string)
    # Iterate through the set of anagrams
    for anagram in anagram_set:
        # Check if there are at most 67 pairs of anagrams in the list
        num_pairs += len(anagram_set) - 1
    return num_pairs <= 67
