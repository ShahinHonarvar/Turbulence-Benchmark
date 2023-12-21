
def filter_chars(string):
    filtered_string = ""
  
    for index, char in enumerate(string):
        if index >= 42 and index <= 97 and char >= "*" and char <= "b":
            continue
        filtered_string += char
      
    return filtered_string
