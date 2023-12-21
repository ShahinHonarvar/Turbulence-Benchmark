
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+74, len(s)+1):
            substring = s[i:j]
            if not set(substring).difference('abcdefghijklmnopqrstuvwxyz'):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
