
def palindromes_of_specific_lengths(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 23 to index 94, both inclusive
    for i in range(23, 95):
        # Check if the substring has length between 17 and 55 (both inclusive)
        if len(string[i:i+55]) >= 17 and len(string[i:i+55]) <= 55:
            # Check if the substring is a palindrome
            if string[i:i+55] == string[i:i+55][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:i+55])
    
    # Return the set of palindromes
    return palindromes
