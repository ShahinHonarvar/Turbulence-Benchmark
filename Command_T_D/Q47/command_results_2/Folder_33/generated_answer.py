def palindromes_of_specific_lengths(s):
    s=s[130: 295].lower()
    return set(s[i:i+104] for i in range(0,len(s)-103))
