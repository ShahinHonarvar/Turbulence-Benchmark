
def palindromes_of_specific_lengths(string):
    palindromes = set()

    substring = string[11:88].lower()

    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i : i + length]
            
            if substring_slice.isalpha() and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)

    return palindromes
