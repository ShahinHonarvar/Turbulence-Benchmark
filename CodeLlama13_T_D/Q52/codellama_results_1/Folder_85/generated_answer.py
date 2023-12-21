
def palindrome_of_length_n(string, n):
    return set([s[i:i+n] for i in range(len(s)) if s[i:i+n].lower() == s[i:i+n][::-1].lower()])
