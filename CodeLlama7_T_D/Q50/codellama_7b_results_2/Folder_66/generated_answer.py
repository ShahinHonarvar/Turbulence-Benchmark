
def if_contains_anagrams(my_list):
    # Check that the input is a list of strings
    if not isinstance(my_list, list) or not all(isinstance(s, str) for s in my_list)):
        raise ValueError("The input must be a list of strings")
    # Initialize variables to keep track of the anagrams
    num_anagrams = 0
    num_anagrams_with_length_of_at_least_three = 0
    for s1 in my_list:
        # Skip over empty strings
        if len(s1) == 0:
            continue

        # Convert the string to lowercase and sort the characters
        s2 = "".join(sorted(s1.lower()))
        # Check if the sorted string is already in the list of anagrams
        if s2 in my_list:
            num_anagrams += 1
            # If the sorted string has a length of at least three, increment the count of anagrams with this property
            if len(s2) >= 3:
                num_anagrams_with_length_of_at_least_three += 1
    # Return true if there are at least 92 pairs of anagrams in the given list; otherwise, return false
    return num_anagrams >= 92 and num_anagrams_with_length_of_at_least_three >= 10
