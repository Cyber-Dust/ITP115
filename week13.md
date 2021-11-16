# OBJECT ORIENTED PROGAMMING IN PY

Object Oriented Programming
* majority of commercial software
* Basic building block is the *object*

Can represent real life objects and abstract objects

Before building an object, Design it

1. Create a *class*
* define class once
* create many objects from the same class

2. In the class, define attribute and methods
* variables = attributes
* functions = methods

Syntax
`
class ClassName: 
  statements
`

Conventions:
* use upper CamelCase
* or upper Snake_Case

ex.) A phone

`
class Mobile_Phone:
  def __init__(self):
    self.make = "Apple"
    self.model = "iPhone5"
  
`

### __init__() Method
* a method that is a constructor
* double underscores = "dunder"

### __str__() Method
* no parameters
* returns a string
* used to print an object make from the class

### Self
* a way for the object to refer to itself
* attributes are porceeded by self
*

CODE EXAMPLE

`
class Mobile_Phone:
  def __init__(self, make, model):
    self.make = make
    self.model = model
    
def main():
  dasean = Mobile_Phone("Apple", "iPhone SE")
  
main()

`


