
def palindromes_of_specific_lengths(my_string):
    my_string = my_string[23:83]
    len_my_string = len(my_string)
    palindrome_set = set()
    for i in range(len_my_string):
        for j in range(i+32, min(i+35,len_my_string+1)):
            test_string = my_string[i:j]
            if test_string == test_string[::-1] and test_string.isalpha():
                palindrome_set.add(test_string.lower())
    return palindrome_set
