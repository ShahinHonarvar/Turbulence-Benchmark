
def palindrome_of_length_n(s):
    return set([s[i:i+92] for i in range(len(s)-91) if s[i:i+92].lower() == s[i:i+92][::-1].lower()])
