
import string

def palindromes_of_specific_lengths(string):
    string = string[:8]
    palindromes = set()
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1] and all(letter in string.ascii_letters for letter in word)
    
    for i in range(len(string)):
        for j in range(i + 4, min(i + 6, len(string) + 1)):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    
    return palindromes
