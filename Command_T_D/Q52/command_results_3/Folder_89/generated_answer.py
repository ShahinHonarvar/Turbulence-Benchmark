def palindrome_of_length_n(s):
    return set(a[i:i+37] for i in range(len(a)) for a in s.lower())
