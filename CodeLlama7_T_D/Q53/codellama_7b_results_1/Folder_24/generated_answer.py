
def palindrome_of_length_at_least_n(input_string, n=53):
    # Convert the input string to lowercase
    input_string = input_string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Get the substring starting from the current index and extending to the end of the input string
        substr = input_string[i:]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes with lengths greater than or equal to n
    return {p for p in palindromes if len(p) >= n}
