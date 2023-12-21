
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 104 to 120 (both inclusive) in the specified index range
    for i in range(155, 283):
        for j in range(i + 103, i + 121):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
