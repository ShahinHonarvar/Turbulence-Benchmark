
def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    palindromes = set()

    for length in range(20, 31):
        for i in range(0, len(s) - length + 1):
            subset = s[i:i+length]
            if subset == subset[::-1] and subset.isalpha():
                palindromes.add(subset)

    return palindromes
