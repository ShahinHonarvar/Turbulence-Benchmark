
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 68):
        substring = s[i:i+69]
        if all(char.isalpha() for char in substring):
            if substring == substring[::-1]:
                result.add(substring)
    return result
