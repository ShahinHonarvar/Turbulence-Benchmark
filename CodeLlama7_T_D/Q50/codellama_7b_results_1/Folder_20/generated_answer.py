
def if_contains_anagrams(my_list):
    # Check that the input is a list of strings
    if not all(isinstance(s, str) for s in my_list)):
        raise ValueError("Input must be a list of strings")
    # Create a dictionary to keep track of anagram pairs
    pair_dict = {}

    for i in range(len(my_list)):

        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower())):
                # If the strings are anagrams, add them to the dictionary
                pair_dict[(my_list[i], my_list[j])] += 1
    # Return True if there are at least 64 pairs of anagrams in the list
    return len(pair_dict) >= 64
