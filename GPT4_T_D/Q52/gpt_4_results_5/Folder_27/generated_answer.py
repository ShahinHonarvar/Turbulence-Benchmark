
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    length = 56
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            results.add(substring)
    return results
