 def palindromes_between_indices(string):
    # Define the range of indices to consider
    start = 1
    end = 6
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each possible substring of length at least 4
    for i in range(start, end + 1 - 3):
        # Get the substring and convert it to lowercase
        substring = string[i:i+4].lower()
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
