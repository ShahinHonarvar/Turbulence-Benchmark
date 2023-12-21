def palindrome_of_length_at_least_n(s):
    return {a for i in range(7, len(s)) for a in s[i:i+2][::-1]]
