
def palindrome_of_length_n(string):
    # Create a list of all substrings of length n in the given string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Return the set of all palindromes in the list of substrings
    return {s for s in substrings if s == s[::-1]}
