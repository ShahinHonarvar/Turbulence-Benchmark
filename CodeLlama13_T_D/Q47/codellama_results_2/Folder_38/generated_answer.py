
def palindromes_of_specific_lengths(string):
    # Initialize the set of palindromes and indices to consider
    palindromes = set()
    start, end = 18, 87
    
    # Iterate through the substring from index 18 to index 87
    for i in range(start, end + 1):
        # Extract the substring at each position
        substr = string[i:i+60]
        
        # Check if the substring is a palindrome of the desired length
        if len(substr) >= 38 and len(substr) <= 60:
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
