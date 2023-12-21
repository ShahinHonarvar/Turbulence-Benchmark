
def palindrome_of_length_n(s):
    return {s[i:i+27] for i in range(len(s)-26) if s[i:i+27].lower() == s[i:i+27][::-1].lower()}
