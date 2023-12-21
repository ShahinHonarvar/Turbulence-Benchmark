
def palindromes_of_specific_lengths(string):
    # Initialize empty set to store palindromes
    palindromes = set()

    # Iterate over substring from index 15 to index 86, both inclusive
    for i in range(15, 87):
        # Iterate over lengths between 51 and 60 (both inclusive)
        for length in range(51, 61):
            # Check if substring from current index to current index + length - 1 is a palindrome
            substring = string[i:i+length]
            if substring == substring[::-1]:
                # Add palindrome to set if it meets the requirements
                palindromes.add(substring)

    return palindromes
