
def palindromes_between_indices(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible combination of 3 letters in the given string that occur between indices 0 and 4, both inclusive
    for i in range(5):
        for j in range(i + 2, 6):
            substring = string[i:j]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    
    return palindromes
