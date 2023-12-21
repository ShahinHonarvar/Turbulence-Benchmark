
def palindromes_of_specific_lengths(string):
    # Find the substring from index 23 to index 82, both inclusive
    substr = string[23:82]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate through each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a letter
        if substr[i].isalpha():
            # Find the length of the palindrome starting from the current character
            length = 1
            while i - length >= 0 and i + length < len(substr) and substr[i - length] == substr[i + length]:
                length += 1
            
            # If the length is between 32 to 34 (both inclusive), add it to the set of palindromes
            if 32 <= length <= 34:
                palindromes.add(substr[i - length + 1:i + length])
    
    return palindromes
