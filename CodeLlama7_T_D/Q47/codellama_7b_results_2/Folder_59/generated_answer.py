
def palindromes_of_specific_lengths(string):
    # Define the length range for palindromes
    min_len = 3
    max_len = 15
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at index j
        substring = string[i:i+max_len]
        # Check if the substring is a palindrome
        if len(substring) >= min_len and len(substring) <= max_len and substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
