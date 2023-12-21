
def palindromes_of_specific_lengths(string):
    # Find the substring from index 11 to index 87, both inclusive
    substr = string[10:88]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 4 and 5 (both inclusive)
    for length in range(4, 6):
        # Iterate over each position in the substring
        for i in range(len(substr)):
            # Check if the substring from index i to index i + length - 1 is a palindrome
            substr_length = substr[i:i+length]
            if substr_length == substr_length[::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substr_length)
    
    return palindromes
