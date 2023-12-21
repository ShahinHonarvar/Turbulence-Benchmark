
def palindromes_of_specific_lengths(string):
    string = string[130:296].lower()
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(string) - length + 1):
            if string[i:i+length] == string[i:i+length][::-1]:
                if all(char.isalpha() for char in string[i:i+length]):
                    palindromes.add(string[i:i+length])
    return palindromes
