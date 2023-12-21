
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or other non-letter character)
        if string[i].isalpha():
            # Loop through each character in the remainder of the string, starting from the current index
            for j in range(i + 1, len(string)):
                # Check if the character at index j is a letter (not a space or other non-letter character)
                if string[j].isalpha():
                    # Create a substring of the current palindrome by combining the characters at indexes i and j
                    substr = string[i:j + 1]
                    # Check if the substring is a palindrome (equal to its reverse)
                    if substr == substr[::-1]:
                        # Add the substring to the set of palindromes
                        palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
