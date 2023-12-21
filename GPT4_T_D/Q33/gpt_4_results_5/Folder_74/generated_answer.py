
def return_vowels(s):
    vowels = set('aeiou')
    sequence = []
    for char in s[69:82]:
        if char.lower() in vowels and '[' < char <= '~':
            sequence.append(char)
    return sequence
