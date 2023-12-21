
def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    palindromes = set()

    for length in range(34, 56):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start+length]

            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)

    return palindromes
