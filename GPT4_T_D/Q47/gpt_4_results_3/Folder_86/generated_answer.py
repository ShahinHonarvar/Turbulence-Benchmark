
def palindromes_of_specific_lengths(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string[30:96])).lower()
    palindromes = set()
    for i in range(len(filtered_string)):
        for j in range(i+34, i+56):
            if j > len(filtered_string):
                break
            substring = filtered_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
