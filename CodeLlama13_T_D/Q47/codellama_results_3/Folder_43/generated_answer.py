
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 41 to index 89, both inclusive
    for i in range(41, 90):
        # Check if the current character is a letter and if it's a palindrome
        if string[i].isalpha() and string[i] == string[i][::-1]:
            # Add the palindrome to the set if it meets the length requirements
            if 23 <= len(string[i]) <= 38:
                palindromes.add(string[i])
    
    # Return the set of all palindromes that meet the requirements
    return palindromes
