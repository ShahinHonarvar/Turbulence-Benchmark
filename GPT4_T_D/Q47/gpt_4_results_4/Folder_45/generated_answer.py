
def palindromes_of_specific_lengths(input_str):
    input_str = input_str[70:141]
    output_set = set()
    for i in range(len(input_str)):
        for j in range(i+3, min(i+61, len(input_str)+1)):
            substring = input_str[i:j]
            if substring == substring[::-1] and substring.isalpha():
                output_set.add(substring.lower())
    return output_set
