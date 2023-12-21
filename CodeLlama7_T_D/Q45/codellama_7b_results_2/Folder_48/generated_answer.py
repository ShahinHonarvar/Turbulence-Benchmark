 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(6, 9):
        # Get the substring of the string that starts at index 6 and ends at index 8
        substring = string[i-2:i+1]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
