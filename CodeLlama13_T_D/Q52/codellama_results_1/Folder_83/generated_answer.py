
def palindrome_of_length_n(s):
    return {s[i:i+24] for i in range(len(s) - 24 + 1) if s[i:i+24].lower() == s[i:i+24][::-1].lower()}
