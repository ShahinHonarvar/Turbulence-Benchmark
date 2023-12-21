def palindromes_between_indices(s):
    idx = next((i for i in range(len(s) - 3) if s[i:i + 3] in s[i + 4:i + 9]), -1)
    if idx == -1:
        return set()
    idx += 4
    return {s[idx:idx + 3] for s[idx:idx + 3] in s[idx + 4:idx + 9] if s[idx:idx + 3] in s[idx + 4:idx + 9]}
