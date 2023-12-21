
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagrams
    anagram_set = set()
    # Iterate through the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lower_string = string.lower()
        # Check if the length of the string is at least 3
        if len(lower_string) >= 3:
            # Sort the characters in the string
            sorted_chars = "".join(sorted(lower_string))
            # If the sorted string is not already in the set, add it to the set
            if sorted_chars not in anagram_set:
                anagram_set.add(sorted_chars)
    # Check if there are at most 47 pairs of anagrams in the set
    return len(anagram_set) <= 47
