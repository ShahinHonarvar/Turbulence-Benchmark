
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagrams and their lengths
    num_anagrams = 0
    min_length = 3

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is an anagram of itself
        if sorted(string) == sorted(string[::-1])):
            # Increment the number of anagrams
            num_anagrams += 1

        # Check if the string is a palindrome
        if string == string[::-1]):
            # If the string is at least three characters long, increment the number of anagrams
            if len(string) >= min_length:
                num_anagrams += 1

    # Return True if there are at least 115 pairs of anagrams in the list; otherwise return False
    return num_anagrams >= 115
