
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[127:289]
    substring = substring.lower()
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes
