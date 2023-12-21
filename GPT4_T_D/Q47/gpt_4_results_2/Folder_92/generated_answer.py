
def palindromes_of_specific_lengths(input_string):
    input_string = input_string[0:5].lower()
    results = set()
    for i in range(len(input_string)):
        for j in range(i + 3, min(i + 5, len(input_string) + 1)):
            substring = input_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                results.add(substring)
    return results
