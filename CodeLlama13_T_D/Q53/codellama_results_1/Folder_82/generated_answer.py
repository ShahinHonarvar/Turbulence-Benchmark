
def palindrome_of_length_at_least_n(string, n):
    # Find all the substrings in the given string that are of length greater than or equal to 72
    substrs = [string[i:j] for i in range(len(string)) for j in range(i + 1, min(i + 73, len(string) + 1))]
    
    # Filter out all the substrings that are not palindromes
    palindromes = [substr for substr in substrs if substr == substr[::-1]]
    
    # Return a set of all palindromes found in the given string
    return set(palindromes)
