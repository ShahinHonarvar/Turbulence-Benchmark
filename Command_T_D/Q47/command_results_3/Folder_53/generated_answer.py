def palindromes_of_specific_lengths(s):
    return set(i[1:-1] for i in range(1, 300) if i in s.lower() and len(i) in range(3, 11))
