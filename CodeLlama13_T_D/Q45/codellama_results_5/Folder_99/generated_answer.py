
def palindromes_between_indices(string):
    # Extract the English letters from the given string
    english_letters = ''.join(c for c in string if c.isalpha() and c.lower() in "abcd")
    
    # Create a set of all palindromes of length at least 3
    palindromes = {english_letters[i:j] for i in range(len(english_letters)-2)
                             for j in range(i+3, len(english_letters)+1)
                             if english_letters[i:j] == english_letters[i:j][::-1]}
    
    # Return the set of palindromes that are created from any possible arrangement of the English letters in the given string that occur between index 4 to index 8, both inclusive.
    return {palindrome for palindrome in palindromes if len(palindrome) >= 3 and all(ord(c)-ord('a') in range(4,9) for c in palindrome)}
