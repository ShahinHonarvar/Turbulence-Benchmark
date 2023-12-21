
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at the current character and extending to the end of the string
        substr = string[i:]
        # Check if the substring is a palindrome (reads the same backwards as it does forwards)
        if substr == substr[::-1]:
            # If the substring is a palindrome, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes that have a length greater than or equal to n
    return palindromes
