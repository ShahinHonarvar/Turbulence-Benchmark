def palindrome_of_length_at_least_n(s):
    return set(s.lower() for i in range(1,len(s)+1) if s[i-1:i+i] == s[i-1:i+i][::-1])
