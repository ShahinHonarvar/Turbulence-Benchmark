def palindromes_between_indices(strng):
    return set(f'{strng[0:7]}.{strng[6:7]}.{strng[5:6]}.{strng[4:5]}.{strng[3:4]}.{strng[2:3]}')
