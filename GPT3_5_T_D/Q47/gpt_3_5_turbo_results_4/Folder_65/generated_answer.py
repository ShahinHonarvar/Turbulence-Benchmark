
import string

def palindromes_of_specific_lengths(s):
    s = s.lower()[15:96]
    palindromes = set()
    
    for length in range(20, 67):
        for start in range(82):  # 82 - (95 - 66)
            substring = s[start:start+length]
            if len(substring) != length:
                break
            if substring == substring[::-1] and all(char in string.ascii_letters for char in substring):
                palindromes.add(substring)
    
    return palindromes
