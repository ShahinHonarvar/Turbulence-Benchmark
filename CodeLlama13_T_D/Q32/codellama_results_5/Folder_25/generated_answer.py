
def insert_after_character(string):
    return ''.join([char if char != 'e' else 'W{}'.format(char) for char in string])
