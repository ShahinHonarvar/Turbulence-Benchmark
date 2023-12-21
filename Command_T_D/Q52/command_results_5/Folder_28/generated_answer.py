def palindrome_of_length_n(s):
    return {i[::-1] for i in range(len(s) - 1, -1, -1) if s[i:i+43][::-1] == s[i:i+43]}
