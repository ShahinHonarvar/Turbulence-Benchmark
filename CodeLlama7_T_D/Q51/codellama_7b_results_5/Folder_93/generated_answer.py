
def if_contains_anagrams(my_list):
    # Define a set of all English letters
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    # Initialize variables to keep track of anagram pairs
    num_pairs = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the current string to lowercase
        lowercase_string = string.lower()
        # Check if the current string is an anagram of another string in the list
        for other_string in my_list:
            # If the current string and another string in the list are not the same string, check if they are anagrams
            if lowercase_string != other_string:
                # Check if the current string is a permutation of the other string
                if sorted(lowercase_string) == sorted(other_string):
                    # If the current string and another string in the list are anagrams, increment the number of anagram pairs found
                    num_pairs += 1
                    # If there are at most 36 pairs of anagrams in the given list, return True
                    if num_pairs <= 36:
                        return True
            # If there are more than 36 pairs of anagrams in the given list, return False
            else:
                return False
