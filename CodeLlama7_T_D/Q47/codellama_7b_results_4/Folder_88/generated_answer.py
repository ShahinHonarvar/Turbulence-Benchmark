
def palindromes_of_specific_lengths(string):
    # Define the substring of interest
    substr = string[11:87]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Define the starting and ending indices of the current substring
        start = i
        end = len(substr) - i

        # Iterate over each length of palindrome to consider
        for length in range(4, 6):
            # Define the substring of interest with the specified length
            substr_length = substr[start:end][:length]
            # Check if the substring is a palindrome in a case-insensitive manner
            if substr_length == substr_length[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr_length)
    # Return the set of palindromes
    return palindromes
