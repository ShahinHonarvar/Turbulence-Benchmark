
def palindrome_of_length_n(s):
    return {p for p in (s[i:j+1] for i in range(len(s) - 9) for j in range(i + 9, len(s))) if p == p[::-1]}
