def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(62, 88) for j in range(i, 88) if len(set(s[i:j])) == 18 or len(set(s[i:j])) == 19 or len(set(s[i:j])) == 20 or len(set(s[i:j])) == 21)
