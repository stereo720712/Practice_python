import random


code = [chr(i) for i in range(97,123)]
random.shuffle(code)
code_str = "".join(code)
print()
print(code_str)
print()

