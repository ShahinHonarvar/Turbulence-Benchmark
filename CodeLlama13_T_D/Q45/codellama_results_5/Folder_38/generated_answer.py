
def palindromes_between_indices(string):
    return set([s[i:j+1] for i in range(3, 8) for j in range(i, 8) if s[i:j+1] == s[j-i:i-1:-1]])
