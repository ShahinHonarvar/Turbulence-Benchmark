
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 100 to index 295, both inclusive
    substring = string[100:296]
    palindromes = []
    for i in range(len(substring)):
        for j in range(i+136, min(i+161, len(substring))):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.append(substring[i:j])
    return set(palindromes)
