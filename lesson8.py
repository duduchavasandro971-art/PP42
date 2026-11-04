#def my_decorator(func, speed):
  #  def wrapper():
  #      print('before')
      #  func()
       # print(f"after {speed}")
#
  #  return wrapper


#def function():
   # print('Decorated function')
def make_multiplier(factor):
    def multiplier(x):
        return x * factor  # 'factor' is remembered
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15