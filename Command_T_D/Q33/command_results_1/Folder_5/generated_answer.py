def return_vowels(str1):
    return [x for x in str1[5:-1] if x.isalpha() and x.lower() in "aeiouAEIOU"]
