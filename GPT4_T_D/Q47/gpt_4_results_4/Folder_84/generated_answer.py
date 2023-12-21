
def palindromes_of_specific_lengths(string):
    string = string[23:78]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+13, min(i+41, len(string) + 1)):
            substr = string[i:j]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes
