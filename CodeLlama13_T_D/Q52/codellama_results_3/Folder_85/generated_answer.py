
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 46 in the given string
    for i in range(len(string) - 46 + 1):
        substring = string[i:i+46]
        
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    # Return the set of all palindromes found in the given string
    return palindromes
