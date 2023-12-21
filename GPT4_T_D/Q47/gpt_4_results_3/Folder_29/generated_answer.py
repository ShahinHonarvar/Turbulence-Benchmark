
def palindromes_of_specific_lengths(input_str):
  import re
  substring = input_str[15:95]
  palindrome_list = set()
  for i in range(len(substring)):
    for length in range(18, 74):
      if i+length > len(substring):
        break
      test_str = substring[i:i+length]
      if test_str.lower() == test_str[::-1].lower() and re.match("^[A-Za-z]*$", test_str):
        palindrome_list.add(test_str)
  return palindrome_list
