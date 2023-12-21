
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)-24+1):
        substring = s[i:i+24]
        if substring == substring[::-1] and substring.isalpha():
            results.add(substring)
    return results
