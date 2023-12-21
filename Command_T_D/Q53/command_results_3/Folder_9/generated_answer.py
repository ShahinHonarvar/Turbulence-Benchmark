def palindrome_of_length_at_least_n(s):
    return {s[i:i+97] for i in range(len(s)-95) if s[i:i+97] == s[i:i+97][::-1]}
