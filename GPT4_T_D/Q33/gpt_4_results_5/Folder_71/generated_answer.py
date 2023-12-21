
def return_vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = []
    for i in range(36,56):
        if s[i] in vowels and '+' < s[i] <= '/':
            result.append(s[i])
    return result
