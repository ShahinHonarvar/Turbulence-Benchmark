
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Split the string into a list of individual characters
        char_list = lowercase_string.split("")
        # Sort the character list alphabetically
        sorted_char_list = sorted(char_list)
        # Check if there are any anagrams in the list by comparing the sorted lists
        if "".join(sorted_char_list) == "abcdefghijklmnopqrstuvwxyz":
            num_anagrams += 1
            if num_anagrams > 81:
                return False

    return True
