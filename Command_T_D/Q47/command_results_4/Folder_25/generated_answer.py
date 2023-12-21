def palindromes_of_specific_lengths(s):
    return set(a[26:84] for a in s[30:-30:-1] if a[0] in 'QWRTYPSDFGHJKLZXCVBNM' and a[1:][::-1] == a[1:])
