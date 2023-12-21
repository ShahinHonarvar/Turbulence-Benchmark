
def palindromes_between_indices(string):
    # Define the range of indices for which palindromes will be created
    start_index = 4
    end_index = 8
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is not a letter
        if not string[i].isalpha():
            continue

        # Create a palindrome by reversing the characters in the string within the specified range
        palindrome = string[start_index:end_index+1]
        # Reverse the order of the characters in the palindrome
        palindrome = palindrome[::-1]
        # Add the palindrome to the set of palindromes if it is at least 5 characters long and does not contain any non-letter characters
        if len(palindrome) >= 5 and all(char.isalpha() for char in palindrome):
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
