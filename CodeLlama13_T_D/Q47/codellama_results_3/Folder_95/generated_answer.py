
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 12 to index 56, both inclusive
    for i in range(12, 57):
        # Check if the substring is a palindrome
        if string[i:i+20] == string[i:i+20][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+20])
    
    return palindromes
