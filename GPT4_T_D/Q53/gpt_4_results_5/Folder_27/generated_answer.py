
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + 100, len(s) + 1):
            slice = s[i:j]
            if slice == slice[::-1] and slice.isalpha():
                palindromes.add(slice)

    return palindromes
