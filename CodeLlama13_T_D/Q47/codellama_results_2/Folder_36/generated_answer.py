
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the substring from index 124 to index 283, both inclusive
    for i in range(124, 284):
        # Check if the current index is a palindrome of the specified length
        if len(string[i]) == 134 and string[i] == string[i][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i])
    
    return palindromes
