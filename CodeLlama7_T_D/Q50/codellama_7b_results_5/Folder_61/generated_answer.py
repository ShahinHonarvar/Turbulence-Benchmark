
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Iterate over the list and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if len(my_list[i]) >= min_length and len(my_list[j]) >= min_length:
                # Check if the two strings are anagrams of each other
                if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                    num_pairs += 1
                    if num_pairs >= 8:
                        return True

    # If no pairs were found, return False
    return False
