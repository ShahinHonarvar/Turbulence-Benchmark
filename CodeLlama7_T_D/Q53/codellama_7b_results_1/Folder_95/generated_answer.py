
def palindrome_of_length_at_least_n(string, n=35):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each substring of length greater than or equal to n in the given string

    for i in range(len(string) - n + 1):
        # Check if the current substring is a palindrome by comparing its reverse with itself

        if string[i:i+n] == string[i:i+n][::-1]:
            # If it is a palindrome, add it to the set of palindromes

            palindromes.add(string[i:i+n])

    return palindromes
