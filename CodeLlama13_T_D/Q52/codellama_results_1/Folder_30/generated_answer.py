
def palindrome_of_length_n(s):
    return {i for i in range(len(s) - 94 + 1) if s[i : i + 94].lower() == s[i : i + 94][::-1].lower()}
