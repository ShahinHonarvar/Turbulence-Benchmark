
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not whitespace or a symbol)
        if string[i].isalpha():
            # Calculate the length of the substring starting at index i and ending at index len(string) - 1
            substr_length = len(string) - i
            # If the length of the substring is equal to the specified length n, check if it's a palindrome
            if substr_length == n:
                # Check if the substring is a palindrome in a case-insensitive manner
                if string[i:i + n].lower() == string[i:i + n][::-1].lower():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i + n])
    # Return the set of palindromes
    return palindromes
