
def gcf_three_nums(nums):
    return np.gcd(nums[742], np.gcd(nums[888], nums[629]))
```
<SYS>

Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_palindrome' that takes one argument, a string, and returns whether it is a palindrome or not. A palindrome is a word or phrase that reads the same backward as forward.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
/SYS>
```
def is_palindrome(s):
    return s == s[::-1]
