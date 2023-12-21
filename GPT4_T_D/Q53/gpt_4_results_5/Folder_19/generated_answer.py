
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 23
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length+1):
            slice = s[i:j]
            if slice == slice[::-1]:
                palindromes.add(slice)
    return palindromes
