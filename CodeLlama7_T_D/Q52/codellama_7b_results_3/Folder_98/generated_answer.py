
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or a punctuation mark)
        if string[i].isalpha():
            # Get the substring of length 6 starting from the current index
            substr = string[i:i+6]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of all palindromes of length 6 as substrings of the given string
    return palindromes
