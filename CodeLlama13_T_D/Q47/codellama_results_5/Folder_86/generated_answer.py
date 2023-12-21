
def palindromes_of_specific_lengths(string):
    # Get the substring from index 30 to index 95, both inclusive
    substring = string[30:96]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i + 30
        
        # Check if the character is an English letter
        if char.isalpha():
            # Find the palindrome of length 34 to 55 (both inclusive) starting from the current index
            for j in range(34, 56):
                palindrome = substring[index:index+j]
                
                # Check if the palindrome is a palindrome and its length is between 34 to 55 (both inclusive)
                if palindrome == palindrome[::-1] and len(palindrome) in range(34, 56):
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    
    # Return the set of palindromes
    return palindromes
