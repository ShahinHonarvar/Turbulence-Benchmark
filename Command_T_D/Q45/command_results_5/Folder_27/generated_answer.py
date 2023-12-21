def palindromes_between_indices(s):
    return {s[i:i+8] for i in range(2, len(s)-1) if s[i:i+8] in (''.join(sorted(set(s[2:8]))), s[2:8].lower())}
