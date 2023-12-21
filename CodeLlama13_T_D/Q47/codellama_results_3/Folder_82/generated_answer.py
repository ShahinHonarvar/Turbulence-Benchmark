
def palindromes_of_specific_lengths(string):
    index = 3
    length = 30
    substring = string[index:index + length]
    palindromes = set()
    for i in range(len(substring)):
        if substring[i].isalpha():
            j = i + 1
            while j < len(substring) and substring[j].isalpha():
                if substring[i] == substring[j]:
                    palindromes.add(substring[i:j+1])
                j += 1
    return palindromes
