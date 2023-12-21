
def palindromes_between_indices(s):
    return { s[i:j] for i in range(3) for j in range(i+3, len(s)+1) if s[i:j] == s[j-1:-i-1][::-1] }
