class Parent():
  def __init__(self):
    self.first_name = "Lorelei"
    self.last_name = "Gilmore"
    print('Parent initialized: ', self)

  def hello(self):
    print(f'Hey, I am {self.first_name}. Welcome to the Dragonfly.')



class Child(Parent):
  def __init__(self):
    #? same as super().__init__() ??
    Parent.__init__(self)
    self.firt_name = "Rory"
    print('Child initialized: ', self)

  def hello(self):
    print(f"I'm {self.first_name}. Can't tlak, late for class!")


mom = Parent()
daughter = Child()

mom.hello()
daughter.hello()

print(daughter.last_name)