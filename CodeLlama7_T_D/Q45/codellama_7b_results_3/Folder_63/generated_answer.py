
def palindromes_between_indices(string):
    # Define the range of indices for the given string
    start = 0
    end = 3
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length 4 starting from index 0
    for i in range(start, end + 1):
        # Extract the substring and reverse it
        substring = string[i:i+4]
        reversed_substring = substring[::-1]
        # Check if the substring is a palindrome
        if substring == reversed_substring:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
