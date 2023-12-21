
def palindromes_of_specific_lengths(string):
    # Only consider palindromes occurring in the substring from index 26 to index 90, both inclusive
    substr = string[26:91]
    
    # Only consider palindromes of lengths between 27 to 58 (both inclusive)
    palindromes = {palindrome for palindrome in substr.split() if len(palindrome) in range(27, 59)}
    
    # Only consider English letters
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = {palindrome for palindrome in palindromes if set(palindrome.lower()) <= english_letters}
    
    # Return the set of all palindromes with the specified requirements
    return palindromes
