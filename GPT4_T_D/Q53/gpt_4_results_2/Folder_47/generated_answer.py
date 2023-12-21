
def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    length = len(s)
    for i in range(length):
        for j in range(i+77, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    return palindrome_set
