
def palindrome_of_length_at_least_n(s):
    return {w for w in s.split() if len(w) >= 52 and all(w[i] == w[-i-1] for i in range(len(w)))}
