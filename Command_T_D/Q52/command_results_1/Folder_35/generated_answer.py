def palindrome_of_length_n(s):
    return set(filter(str.lower().__istring__(), (s[i:i + 116] for i in range(0, len(s) - 115))))
