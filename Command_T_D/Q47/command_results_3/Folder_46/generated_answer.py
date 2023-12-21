def palindromes_of_specific_lengths(s):
    return set(x for x in s[11:-11] if x[0] in 'QWRTYPSDFGHJKLZXCVBNM' and x[1:][::-1] == x[:-1])
