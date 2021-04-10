
class Calculator:

  def __init__(self):
    pass

  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

  def subtract(self, a, b):
    return a - b

  def divide(self, a, b):
    if b==0: 
        return "You can t divide by zero!" 
    else: 
        return a/b

def add_all(int_list):
    sum = 0
    for n in int_list:
        sum = sum + n
    return sum
