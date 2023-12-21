
def palindrome_of_length_n(s):
    s = s.lower() #case-insensitive
    length = len(s)
    palindromes = set()
    
    def is_palindrome(string):
        return string == string[::-1]
    
    for i in range(length):
        if i+6 <= length: #to get substrings of length 6
            substring = s[i:i+6] 
            if is_palindrome(substring):
                if substring.isalpha(): #string consisting only of English letters.
                    palindromes.add(substring)
    return palindromes
