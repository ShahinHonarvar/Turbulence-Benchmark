
def palindromes_of_specific_lengths(s):
    sub_string = s[65:100]
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i+26,i+34):
            if j <= len(sub_string):
                sub_str2 = sub_string[i:j]
                if sub_str2 == sub_str2[::-1] and sub_str2.isalpha() and sub_str2.lower() == sub_str2[::-1].lower():
                    palindromes.add(sub_str2)
    return palindromes
