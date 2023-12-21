
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+68, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and all(char.isalpha() for char in substring):
                result.add(substring)
    return result
