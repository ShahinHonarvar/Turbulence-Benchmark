
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+51, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and s[i:j+1].isalpha():
                palindrome_set.add(s[i:j+1])
    return palindrome_set
