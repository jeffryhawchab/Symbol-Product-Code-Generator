import random
import string

symbols = string.punctuation

def generate_product_code():
  code = ""
  for i in range(10):
    code += random.choice(symbols)
  return code

product_codes = set()
while len(product_codes) < 100:
  code = generate_product_code()
  product_codes.add(code)

print(product_codes)



