
def palindrome_of_length_n(s):
    s = s.lower()
    english_characters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    
    for i in range(len(s) - 406):
        substring = s[i:i+407]
        if all(char in english_characters for char in substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
