
def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    substring = input_string[1:300]

    for length in range(3,11):
        for i in range(0, len(substring)-length+1):  
            test_string = substring[i:i+length]
            if test_string == test_string[::-1]:
                test_string = ''.join(filter(str.isalpha, test_string))
                if len(test_string) == length:
                    palindromes.add(test_string.lower())

    return palindromes
