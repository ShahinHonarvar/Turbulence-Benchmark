def palindrome_of_length_at_least_n(s):
    return set(p for p in (s[i:j] for i in range(1,len(s)-1) for j in range(i,len(s)-1)) if p.lower() == p[::-1].lower())
