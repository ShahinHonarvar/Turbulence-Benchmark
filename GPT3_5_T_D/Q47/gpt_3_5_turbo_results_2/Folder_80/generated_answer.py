
def palindromes_of_specific_lengths(string):
    substring = string[35:89].lower()
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(substring) - length + 1):
            current = substring[i:i+length]
            if current == current[::-1] and current.isalpha():
                palindromes.add(current)
    return palindromes
