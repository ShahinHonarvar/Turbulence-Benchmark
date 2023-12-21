
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i + 10, min(len(string), i + 51)):
            if string[i:j].isalpha():
                if string[i:j] == string[i:j][::-1]:
                    palindromes.add(string[i:j])
    return palindromes
