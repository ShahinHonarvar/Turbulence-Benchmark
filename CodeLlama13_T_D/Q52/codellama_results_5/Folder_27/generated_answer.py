
def palindrome_of_length_n(s):
    return {s[i:i+56] for i in range(len(s)-55) if s[i:i+56] == s[i:i+56][::-1]}
