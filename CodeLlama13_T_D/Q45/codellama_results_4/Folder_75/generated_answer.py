
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible combination of letters between indices 2 and 4, both inclusive
    for i in range(len(string) - 3 + 1):
        for j in range(i + 3):
            # Check if the current substring is a palindrome
            if string[i] == string[j]:
                # Add the palindrome to the set
                palindromes.add(string[i:j+1])
    
    return palindromes
