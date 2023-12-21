def palindrome_of_length_n(s):
    return set(s[i:i+41].lower() for i in range(len(s)-40) if s[i:i+41] == s[i][::-1])
