
def palindromes_of_specific_lengths(string):
    lengths = range(12, 15) # Only consider palindromes of these lengths
    substring = string[18:89] # Consider only the substring from index 18 to index 88
    palindromes = set() # Initialize an empty set to store the palindromes
    
    for length in lengths:
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1]: # Check if substr is a palindrome
                palindromes.add(substr)
    
    return palindromes
