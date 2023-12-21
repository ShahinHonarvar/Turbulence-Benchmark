def palindrome_of_length_n(s):
    return {i for i in range(len(s)) if s[i] in 'qwertyuiopasdfghjklzxcvbnm' and s[i][::-1] == s[i]}
