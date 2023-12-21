
def palindrome_of_length_n(s):
    s = s.lower()
    substrings = set()
    for i in range(len(s)):
        for j in range(257, len(s[i:]) + 1):
            if s[i:i + j] == s[i:i + j][::-1]:
                if s[i:i+j].isalpha():
                    substrings.add(s[i:i+j])
    return substrings
