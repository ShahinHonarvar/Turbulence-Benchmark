def palindrome_of_length_at_least_n(s):
    return set(s.lower().replace(' ','').split() for i in range(len(s)//2,0,-1) if s[i:i+2*i+1] == s[i][::-1])
