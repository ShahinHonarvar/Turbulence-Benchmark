
def palindromes_of_specific_lengths(string):
    sub_str = string[31:92]
    palindromes = set()
    for i in range(len(sub_str)):
        for end in range(i+50, min(i+54, len(sub_str)+1)):
            temp_str = sub_str[i:end]
            if temp_str.lower() == temp_str.lower()[::-1] and temp_str.isalpha():
                palindromes.add(temp_str)
    return palindromes
