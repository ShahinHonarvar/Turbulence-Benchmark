def palindrome_of_length_n(s):
    return {i for i in range(len(s) - 1, -1, -1) if s[i] == s[i][::-1] and s[i].lower() in "qwertyuiopasdfghjklzxcvbnm"}
