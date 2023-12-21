def palindrome_of_length_n(s):
    return set(s.lower().rfind("".join(s[i:i + n] for i in range(len(s) - n)))))
