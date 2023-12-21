
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize variables to keep track of anagram pairs
    num_pairs = 0
    previous_string = ""

    # Iterate over the list and check for anagrams
    for string in my_list:
        if string != previous_string:
            # Check if the string is an anagram of the English letters
            if sorted(string.lower()) == sorted("abcdefghijklmnopqrstuvwxyz"):
                # Check if the string has a length of at least three
                if len(string) >= 3:
                    # Increment the number of anagram pairs
                    num_pairs += 1

    # Return whether there are at most 423 pairs of anagrams in the given list
    return num_pairs <= 423
