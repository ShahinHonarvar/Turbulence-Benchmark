
def palindrome_of_length_n(string):
    # Use a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 19 in the given string
    for i in range(len(string) - 18):
        substr = string[i:i+19]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
