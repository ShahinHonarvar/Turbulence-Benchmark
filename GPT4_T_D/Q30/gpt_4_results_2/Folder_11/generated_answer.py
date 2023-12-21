
def insert_before_character(my_str):
    new_str = ""
    for i in my_str:
        if i == 'g':
            new_str += 't'
        new_str += i
    return new_str
