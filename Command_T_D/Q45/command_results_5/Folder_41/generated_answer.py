def palindromes_between_indices(s):
    res = set()
    if s[1] in 'AEIOU' and s[2] in 'AEIOU' and s[3] in 'AEIOU':
        res.add(''.join(sorted(s[1:3])))
    if s[1] in 'aeiou' and s[2] in 'aeiou' and s[3] in 'aeiou':
        res.add(''.join(sorted(s[1:3])))
    return res
