
def palindromes_of_specific_lengths(string):
    # Initialize empty set for storing palindromes
    palindromes = set()
    
    # Iterate through the substring from index 124 to index 283, both inclusive
    for i in range(124, 284):
        # Get the substring from the current index to the next index - 1
        substring = string[i:i+1]
        
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If the substring is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    
    return palindromes
