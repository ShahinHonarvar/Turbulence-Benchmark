
def palindrome_of_length_at_least_n(string, n=144):
    # Convert to lowercase for case-insensitive comparison
    string = string.lower()
    # Initialize the set of palindromes
    palindromes = set()
    # Iterate over all substrings of length greater than or equal to n in the given string
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        # Check if the substring is a palindrome by comparing it to its reverse
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
