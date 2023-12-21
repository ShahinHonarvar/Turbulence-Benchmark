def palindromes_between_indices(s):
    return set(i for i in range(4, len(s) + 1) if i == sum(1 for j in range(i) if s[j] in 'qwertyuiopasdfghjklzxcvbnm'))
