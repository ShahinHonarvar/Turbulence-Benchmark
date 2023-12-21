
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of the number of anagrams and their length
    num_anagrams = 0
    anagram_length = 0

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome (i.e., reads the same backward as forward)
        if lowercase_string == lowercase_string[::-1]:
            # If it is a palindrome, increment the number of anagrams and its length
            num_anagrams += 1
            anagram_length += len(lowercase_string)

    # Return true if there are at least 79 pairs of anagrams in the given list; otherwise, return false
    if num_anagrams >= 79:
        return True
    else:
        return False
