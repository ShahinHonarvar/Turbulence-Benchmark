
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 40
    palindromes = set()

    for size in range(n, len(s) + 1):
        for i in range(0, len(s) - size + 1):
            slice = s[i:i + size]
            if slice == slice[::-1]:
                palindromes.add(slice)
    
    return palindromes
