
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 10
    end = 59
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the specified range
    for i in range(start, end + 1):
        # Check if the substring is a palindrome
        if string[i - 10:i] == string[i - 10:i][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 10:i])
    # Return the set of palindromes
    return palindromes
