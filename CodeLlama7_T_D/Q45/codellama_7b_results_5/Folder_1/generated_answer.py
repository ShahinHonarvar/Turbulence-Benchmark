 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index in the range of 4 to 7 (both inclusive)
    for start_index in range(4, len(input_string) - 2):
        # Initialize a substring with the length of 5 starting from the current starting index
        substring = input_string[start_index:start_index + 5]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
