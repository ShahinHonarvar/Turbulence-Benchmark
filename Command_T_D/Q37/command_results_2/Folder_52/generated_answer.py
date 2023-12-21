 
import re
def filter_chars(text):
    return re.sub(r'(?i)(?<=.)j(?!i).+(?<=.)v(?!i).+(?=.)', '', text)
