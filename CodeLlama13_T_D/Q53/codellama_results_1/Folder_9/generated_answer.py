
def palindrome_of_length_at_least_n(string):
    # Create a list of all the substrings in the string that are at least 95 characters long
    substrs = [substring for substring in string if len(substring) >= 95]
    
    # Create a set to store the palindromes found in the string
    palindromes = set()
    
    # Loop through each substring and check if it is a palindrome
    for substr in substrs:
        if substr == substr[::-1]:
            palindromes.add(substr)
            
    return palindromes
