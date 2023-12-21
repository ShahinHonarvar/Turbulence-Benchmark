
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= 108:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return num % fibonacci[107] == 0
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'decimal_to_binary' that takes one argument, an integer or a string representation of an integer. The function should return a binary representation of the given integer as a string. For example, if the input is 10, the output should be "1010".> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def decimal_to_binary(num):
    return bin(int(num))[2:]
