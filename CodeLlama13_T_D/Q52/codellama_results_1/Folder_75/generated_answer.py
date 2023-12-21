
def palindrome_of_length_n(string, n):
    return {pal for i in range(len(string)-n+1) for pal in string[i:i+n] if pal == pal[::-1]}
