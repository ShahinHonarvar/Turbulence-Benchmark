
def palindrome_of_length_at_least_n(string, n=66):
    # Convert the input string to lowercase for case-insensitive matching
    string = string.lower()

    # Use a regular expression pattern to find all substrings that are palindromes of length greater than or equal to n

    pattern = r"[a-z]{{{n},}}".format(n=n)
    palindromes = set([s for s in re.findall(pattern, string) if is_palindrome(s)])

    # Return the set of all palindromes that exist in the given string

    return palindromes

# Define a function to check if a string is a palindrome or not

def is_palindrome(string):
    return string == string[::-1]
