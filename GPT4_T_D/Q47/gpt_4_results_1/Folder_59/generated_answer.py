
def palindromes_of_specific_lengths(in_str):
    in_str = in_str[:101].lower()
    palindromes = set()
    for i in range(len(in_str)):
        for j in range(i + 3, min(i + 16, len(in_str) + 1)):
            substring = in_str[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
