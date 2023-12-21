
def palindromes_of_specific_lengths(s):
    s = s[30:85]
    subsets = {s[i: j] for i in range(len(s)) 
              for j in range(i + 1, len(s) + 1)}
    palindromes = set()
    for i in subsets:
        if 12<=len(i)<=20 and i == i[::-1] and i.isalpha():
            palindromes.add(i.lower())
    return palindromes
