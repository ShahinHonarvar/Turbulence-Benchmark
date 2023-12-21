
def palindromes_of_specific_lengths(input_string):
    input_string = input_string[63:71]
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(4, 6):
            if (i+j) <= len(input_string):
                substring = input_string[i:i+j]
                if substring.lower() == substring[::-1].lower() and substring.isalpha():
                    palindromes.add(substring)
    return palindromes
