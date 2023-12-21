
def palindromes_of_specific_lengths(string):
    string = string[31:75]
    palindromes = set()
    for length in range(23, 40):
          for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
