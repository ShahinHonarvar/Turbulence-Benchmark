
def palindrome_of_length_n(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the input string
    for i in range(len(input_string) - 99 + 1):
        # Extract the current substring of length n
        substring = input_string[i:i+99]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
