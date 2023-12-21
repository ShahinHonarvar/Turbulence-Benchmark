
def palindromes_of_specific_lengths(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 39-52 in the given string
    for i in range(16, 94+1):
        for j in range(i, min(len(string), i + 17)):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of all palindromes found
    return palindromes
