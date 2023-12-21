
def palindromes_of_specific_lengths(string):
    string = string[:21]
    string = ''.join(filter(str.isalpha, string)).lower()
    results = set()
    for length in range(5, 81):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                results.add(substring)
    return results
