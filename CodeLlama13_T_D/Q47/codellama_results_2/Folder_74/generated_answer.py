
def palindromes_of_specific_lengths(string):
    # Only consider palindromes with lengths between 12 and 20 (both inclusive)
    # and that occur within the substring from index 30 to index 84, both inclusive
    palindromes = {palindrome for palindrome in string[30:85] if len(palindrome) >= 12 and len(palindrome) <= 20}
    
    # Only consider English letters
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = {palindrome for palindrome in palindromes if all(letter in english_letters for letter in palindrome)}
    
    return palindromes
