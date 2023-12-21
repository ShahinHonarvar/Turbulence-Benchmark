
def palindromes_of_specific_lengths(string):
    # Define the set of all palindromes found in the substring from index 125 to index 283, both inclusive
    palindromes = set()
    
    # Loop through each character in the specified substring
    for i in range(125, 284):
        # Check if the current character is a letter and if it is a palindrome of length between 109 to 126 (both inclusive)
        if string[i].isalpha() and len(string[i]) in range(109, 127):
            # Add the palindrome to the set
            palindromes.add(string[i])
    
    return palindromes
