 
import re
def filter_chars(string):
    return re.sub(r'(?<=.)[58-81](?<=.)>5', '', string)
