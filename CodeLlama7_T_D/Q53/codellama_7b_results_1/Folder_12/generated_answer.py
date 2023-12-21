
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the index of the last occurrence of the character in the string
            last_index = len(string) - 1 - string[::-1].find(string[i])
            # Check if the character appears at least n times in the string
            if last_index - i + 1 >= n:
                # Add the palindrome to the set
                palindromes.add(string[i:last_index+1])
    # Return the set of palindromes
    return palindromes
