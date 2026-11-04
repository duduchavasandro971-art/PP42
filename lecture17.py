#class BankAccount:
   # def __init__(self, name, bank, balance) -> None:
      #  self.name: Any = name
      #  self._bank: Any = bank
       # self.__balance: Any = balance
#
  #  @property
  ##  def balance(self) -> Any:
      #  return self.__balance


#acc = BankAccount("John", "Step", 1000)

#print(acc.balance)



class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self) -> None:
        print(f"{self.name} is eating")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping")

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


#class Dog(Animal):
   # def __init__(self, name, age, color) -> None:
     #   super().__init__(name, age)
        self.color = color

  #  def bark(self) -> None:
        print(f"{self.name} is barking")

#class Cat(Animal):
      #def __init__(self, name, age,eye_color) -> None:
            super().__init__(name, age)
           # self.eye_color = eye_color

      #def meow(self) -> None:
        #  print(f"{self.name} is meow, meowing")
       ##   cat_1 = Cat("Tom", 1, "Brown")
        #  print(cat_1)
         # cat_1.eat()
        ##  cat_1.sleep()
         # cat_1.meow()
        #  print(cat_1.eye_color)



#class GoldenRetriever(Dog):
   # def_init(self) -> None:
      #  print(f"{self.name} is playing")






# GoldenRetriever object
#gr_1 = GoldenRetriever("Bob", 2, "Black")
#print(gr_1)
#gr_1.eat()
#gr_1.sleep()
##gr_1.bark()
#gr_1.play()
#print(gr_1.color)


class shape:
    def area(self)
        raise NotImplementedError
