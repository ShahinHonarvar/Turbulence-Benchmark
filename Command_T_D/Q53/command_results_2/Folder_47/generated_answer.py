def palindrome_of_length_at_least_n(s):
    return set(s[i:i + 77] for i in range(len(s) - 77) if s[i:i + 77] == s[i:i + 77][::-1])
