
def palindrome_of_length_n(string):
    # Check if the input string is valid
    if not string or len(string) < n:
        return set()

    # Create a list of all substrings of length n in the input string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]

    # Return the set of palindromes found in the substrings
    return {s for s in substrings if s == s[::-1]}
