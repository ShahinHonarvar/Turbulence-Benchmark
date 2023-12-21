
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 124 to index 283, both inclusive
    for i in range(124, 284):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Find the palindrome of length between 115 to 134 (both inclusive) starting from the current index
            for j in range(i, i+116):
                if len(string[j]) == 134:
                    # Add the palindrome to the set
                    palindromes.add(string[j])
    
    # Return the set of palindromes
    return palindromes
