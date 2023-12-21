def palindrome_of_length_n(s):
    return set(i[i[0] == s[i[0]:i[1]] for i in range(1, len(s) + 1))
