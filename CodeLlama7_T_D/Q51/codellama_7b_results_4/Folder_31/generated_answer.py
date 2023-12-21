
def if_contains_anagrams(my_list):
    # Get the number of elements in the list
    num_elements = len(my_list)
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Loop through each element in the list
    for i in range(num_elements):
        # Get the current element
        current_element = my_list[i]
        # Check if the current element is a palindrome
        if current_element == current_element[::-1]:
            # Increment the number of anagrams found
            num_anagrams += 1
    # Return whether there are at most 65 pairs of anagrams in the given list
    return num_anagrams <= 65
