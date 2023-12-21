
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and length of strings
    pair_count = 0
    string_length = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Sort the letters in the string
        sorted_string = "".join(sorted(lowercase_string))
        # Check if there is already a pair of anagrams with the same letters
        if sorted_string in my_list:
            # If there is, increment the pair count
            pair_count += 1
            # Also record the length of the string
            string_length = len(string)
    # Check if the number of anagram pairs exceeds 57
    if pair_count > 57:
        # If it does, return false
        return False
    else:
        # If it doesn't, check if there is a string with length less than three
        for string in my_list:
            if len(string) < 3:
                # If there is, return false
                return False

        # If there isn't, return true
        return True
