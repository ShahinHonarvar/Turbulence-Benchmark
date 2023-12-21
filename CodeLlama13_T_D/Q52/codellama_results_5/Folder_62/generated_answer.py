
def palindrome_of_length_n(string, n):
    return set([s[i:j] for i in range(len(s)-n+1)
