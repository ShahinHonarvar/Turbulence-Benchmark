def palindrome_of_length_n(s):
    return set(s[i:j] for i in range(0, len(s)-1) for j in range(i+1, len(s)))
