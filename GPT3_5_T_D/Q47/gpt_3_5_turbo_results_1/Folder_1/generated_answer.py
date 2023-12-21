
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:90]
    for length in range(40, 73):
        for i in range(len(substring) - length + 1):
            lowercase = substring[i:i+length].lower()
            if lowercase == lowercase[::-1] and lowercase.isalpha():
                palindromes.add(lowercase)
    return palindromes
