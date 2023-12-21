
def palindromes_of_specific_lengths(string):
    # Get the substring from index 100 to index 295, both inclusive
    substr = string[100:296]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a letter of the alphabet
        if substr[i].isalpha():
            # Get the length of the palindrome starting from the current index
            length = len(palindromes_of_specific_lengths(substr[i:]))
            
            # Check if the length is between 136 and 160, both inclusive
            if 136 <= length <= 160:
                # Add the palindrome to the set
                palindromes.add(substr[i-length+1:i+1])
    
    # Return the set of palindromes
    return palindromes
