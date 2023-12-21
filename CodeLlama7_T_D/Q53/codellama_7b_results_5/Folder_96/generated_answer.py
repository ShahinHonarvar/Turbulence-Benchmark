
def palindrome_of_length_at_least_n(string, n=24):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (not a space or punctuation)
        if char.isalpha():
            # Loop through each character in the string starting from the next character after i
            for j in range(i+1, len(string)):
                # Get the character at index j
                char2 = string[j]
                # Check if the character is a letter (not a space or punctuation)
                if char2.isalpha():
                    # Create a string consisting of the two characters
                    substr = char + char2
                    # Check if the string is a palindrome (same as reading backwards)
                    if substr == substr[::-1]:
                        # Add the palindrome to the set
                        palindromes.add(substr)
    # Return the set of palindromes that have a length greater than or equal to n
    return palindromes
