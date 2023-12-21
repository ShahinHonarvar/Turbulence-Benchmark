def palindromes_between_indices(s):
    return set(
        (s[i:j] for i in range(len(s)-5,len(s)-4) for j in range(i+5,i+9))
        if all(c.lower() in 'qwertyuiopasdfghjklzxcvbnm' for c in s[i:j])
    )
