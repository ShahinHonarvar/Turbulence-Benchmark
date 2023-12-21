
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string that occur between indices 4 and 9, both inclusive
    for letter in string[4:10]:
        # Check if the current letter is a lowercase or uppercase letter of an English alphabet
        if letter.isalpha():
            # Add the palindrome to the set
            palindromes.add(letter)
    
    return palindromes
