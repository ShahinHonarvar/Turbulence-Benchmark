
def palindromes_of_specific_lengths(string):
    string = string[1:9]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 3, min(i + 5, len(string) + 1)):
            sub_string = string[i:j]
            if sub_string.lower() == sub_string[::-1].lower():
                if sub_string.isalpha():
                    palindromes.add(sub_string)
    return palindromes
