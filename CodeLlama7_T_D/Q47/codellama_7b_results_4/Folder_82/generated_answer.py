
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(3, 301):
        # Check if there is a palindrome of length i in the substring
        substr = string[i - 3:i + 3]
        if substr == substr[::-1]:
            # If there is a palindrome, add it to the set
            palindromes.add(substr)
    return palindromes
