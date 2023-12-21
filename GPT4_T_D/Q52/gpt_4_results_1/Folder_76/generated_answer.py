
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s) - 256):
        substring = s[i:i+257]
        if substring == substring[::-1] and substring.isalpha():
            results.add(substring)
    return results
