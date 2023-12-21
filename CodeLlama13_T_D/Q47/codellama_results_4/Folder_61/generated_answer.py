
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 20-30 in the given string
    for i in range(0, len(string) - 21, 1):
        for j in range(i + 20, min(len(string), i + 31)):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    return palindromes
