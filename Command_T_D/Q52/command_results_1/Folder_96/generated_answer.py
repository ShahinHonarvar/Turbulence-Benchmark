def palindrome_of_length_n(s):
    return set(s[i:i+83] for i in range(len(s) - 83) if s[i:i+83] == s[i:i+83][::-1])
