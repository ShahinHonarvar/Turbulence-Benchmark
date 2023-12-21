def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    let = set(str(s[3:5]).lower())
    return set(f" {i[::-1]} " for i in range(len(let) + 1) if i == len(let) + 1 or i == 0)
