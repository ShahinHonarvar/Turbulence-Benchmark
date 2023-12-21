
def palindromes_of_specific_lengths(input_string):
    input_string = input_string[1:8].lower()
    palindromes = set()

    for i in range(len(input_string)):
        for j in range(i + 3, min(len(input_string) + 1, i + 5)):
            sub = input_string[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)

    return palindromes
