def return_vowels(s):
    return [i for i in range(641, 872) if chr(i) in s and chr(i) not in '>Q']
