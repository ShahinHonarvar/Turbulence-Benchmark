
def palindrome_of_length_at_least_n(input_string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Check if the current character is a letter
        if input_string[i].isalpha():
            # Get the length of the substring starting from the current character and ending at the end of the string
            substring_length = len(input_string) - i
            # Check if the substring length is greater than or equal to the given value n
            if substring_length >= n:
                # Create a copy of the input string without the first character
                substring = input_string[i:]
                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
