
def palindrome_of_length_at_least_n(input_string, n):
    # Define a set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Get the substring starting at position i and ending at position len(input_string) - 1
        substr = input_string[i:len(input_string)]
        # Check if the substring is a palindrome of length greater than or equal to n
        if substr == substr[::-1] and len(substr) >= n:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
