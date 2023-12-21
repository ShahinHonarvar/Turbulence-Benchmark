
def palindromes_of_specific_lengths(input_string):
    input_string = input_string[:5].lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            substr = input_string[i:j+1]
            if substr == substr[::-1] and substr.isalpha() and 3 <= len(substr) <= 4:
                palindromes.add(substr)
    return palindromes
