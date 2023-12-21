def return_vowels(s):
    return [i for i in range(63, 79) if chr(i) in s and chr(i) not in 'DghklMPqys']
