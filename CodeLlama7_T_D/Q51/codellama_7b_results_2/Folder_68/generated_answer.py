
def if_contains_anagrams(my_list):
    # Initialize a set to store all anagrams
    anagram_set = set()
    # Iterate over each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if there are at most 94 pairs of anagrams in the given list
        if len(anagram_set) < 94:
            # Add the anagram to the set
            anagram_set.add(lowercase_string)
    # Return True if there are at most 94 pairs of anagrams in the given list; otherwise, return False
    return len(anagram_set) < 94
