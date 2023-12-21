
def palindrome_of_length_n(s):
    s = s.lower()
    length = 9
    pairs = set()
    for i in range(len(s)):
        if i + length > len(s):
            break
        substring = s[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            pairs.add(substring)
    return pairs
