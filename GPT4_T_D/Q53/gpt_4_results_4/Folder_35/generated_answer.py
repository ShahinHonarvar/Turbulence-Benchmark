
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindrome_set = {s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j]==s[i:j][::-1] if len(s[i:j]) >= 26}
    return palindrome_set
