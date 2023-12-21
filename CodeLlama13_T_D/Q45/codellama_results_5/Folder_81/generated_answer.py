
def palindromes_between_indices(string):
    # Get the English letters from the given string
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string that occur between indices 0 and 6, both inclusive
    for i in range(7):
        for j in range(i+3, len(string)+1):
            substr = string[i:j]
            if substr[::-1] == substr and set(substr) <= english_letters:
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
