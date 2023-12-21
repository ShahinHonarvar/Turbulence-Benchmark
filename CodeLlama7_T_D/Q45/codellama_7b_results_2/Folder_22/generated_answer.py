
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(5, len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a new string with the letters between index 5 and index 6 (inclusive)
            substr = string[5:i+1]
            # Check if the new string is a palindrome of length at least 3
            if substr == substr[::-1] and len(substr) >= 3:
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
