
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length at least 4 in the input string
    for i in range(len(input_string) - 3):
        # Extract the substring of length at least 4 from the input string starting at index i
        substring = input_string[i:i+4]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of all palindromes of length at least 4 in the input string that occur between index 1 to index 4, both inclusive
    return palindromes
