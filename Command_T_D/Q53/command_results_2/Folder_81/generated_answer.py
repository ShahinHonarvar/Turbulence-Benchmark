def palindrome_of_length_at_least_n(s):
    return {i for i in range(1,len(s)//2+1) if s[i-1:i+2].lower() == s[i-1:i+2].lower() }
