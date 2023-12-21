
def if_contains_anagrams(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # Get the current element
        current_element = my_list[i]

        # Check if the current element is already in the dictionary
        if current_element in anagram_pairs:
            # If it is, increment the count for this pair
            anagram_pairs[current_element] += 1

        else:
            # If it's not, add a new key to the dictionary with a value of 1
            anagram_pairs[current_element] = 1

    # Iterate over the dictionary and check for pairs that have a count of at least 3
    for key in anagram_pairs:
        if anagram_pairs[key] >= 3:
            return True

    # If we reach this point, there are no pairs with a count of at least 3
    return False
