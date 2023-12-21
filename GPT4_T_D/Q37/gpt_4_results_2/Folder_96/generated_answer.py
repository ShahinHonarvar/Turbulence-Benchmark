
def filter_chars(my_string):
    filtered_chars = set([char for index, char in enumerate(my_string) 
                          if 86 <= index <= 92 and '!' <= char <= 's'])
                          
    return ''.join([char for char in my_string if char not in filtered_chars])
