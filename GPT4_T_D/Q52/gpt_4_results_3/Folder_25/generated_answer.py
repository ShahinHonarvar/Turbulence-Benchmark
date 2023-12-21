
def palindrome_of_length_n(s):
    s = s.lower()
    palindroms = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) == 90 and s[i:j] == s[i:j][::-1]:
                palindrom = s[i:j]
                if palindrom.isalpha():
                    palindroms.add(palindrom)
    return palindroms
