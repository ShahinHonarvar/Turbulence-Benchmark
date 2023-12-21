def palindrome_of_length_n(s):
    return {i for i in range(len(s)) if s[i] in 'QWRTYPSDFGHJKLZXCVBNM' and s[i] == s[i][::-1].lower()}
