def palindrome_of_length_n(s):
    return set(s[i:j] for i in range(len(s) - 1) for j in range(i + 1, len(s) + 1) if s[i:j].lower() == s[i:j][::-1].lower())
