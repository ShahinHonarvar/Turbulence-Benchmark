
def palindromes_between_indices(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible combination of letters between indices 6 and 9
    for i in range(len(string) - 5):
        for j in range(i + 1, len(string)):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    return palindromes
