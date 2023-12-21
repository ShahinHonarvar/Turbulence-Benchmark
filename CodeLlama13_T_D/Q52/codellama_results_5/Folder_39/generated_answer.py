
def palindrome_of_length_n(s):
    return {palindrome for i in range(len(s) - 58) if s[i:i+60] == s[i:i+60][::-1] for palindrome in [s[i:i+60]]}
