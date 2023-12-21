
 def return_n_smallest_chars(string):
     return sorted(list(string), key=lambda x: ord(x), reverse=True)[:70]
