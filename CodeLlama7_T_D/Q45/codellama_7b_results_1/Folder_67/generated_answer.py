 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length 5 in the input string
    for i in range(len(input_string) - 4):
        # Extract the substring from index i to index i + 4
        substring = input_string[i:i + 5]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
