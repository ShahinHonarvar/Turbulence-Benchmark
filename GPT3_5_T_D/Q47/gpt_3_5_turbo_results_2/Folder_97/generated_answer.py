
def palindromes_of_specific_lengths(string):
    substring = string[28:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice.lower() == substring_slice.lower()[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes
