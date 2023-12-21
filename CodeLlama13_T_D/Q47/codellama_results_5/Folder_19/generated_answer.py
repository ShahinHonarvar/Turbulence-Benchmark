
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    substr = string[10:56]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 3 and 7 (both inclusive)
    for length in range(3, 8):
        # Iterate over each position in the substring
        for i in range(len(substr)):
            # Check if the substring from position i to position i + length is a palindrome
            if substr[i:i+length] == substr[i:i+length][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substr[i:i+length])
    
    return palindromes
