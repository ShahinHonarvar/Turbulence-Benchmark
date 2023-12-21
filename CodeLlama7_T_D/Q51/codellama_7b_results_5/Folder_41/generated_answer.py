
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is a palindrome
        if is_palindrome(curr_str):
            # Increment the number of anagrams
            num_anagrams += 1
    # Return whether there are at most 52 pairs of anagrams in the list
    return num_anagrams <= 52
# Check if a string is a palindrome
def is_palindrome(str):
    # Convert the string to lowercase
    lowercase = str.lower()
    # Return whether the converted string is the same as the original string
    return lowercase == str
