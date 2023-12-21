
def palindromes_of_specific_lengths(string):
    string = string[43:96]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+18, min(i+48, len(string)+1)):
            substring = string[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
