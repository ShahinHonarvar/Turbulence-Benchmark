
def palindromes_between_indices(s):
    return {f"{s[i-8:i+1]}".lower() for i in range(9, len(s)) if f"{s[i-8:i+1]}".lower() == f"{s[i-8:i+1]}".lower()[::-1]}
