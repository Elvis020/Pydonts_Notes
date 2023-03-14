# str and repr
* Python has 2 mechanisms that allows you to convert an object to a string and then print it out
* They are:
  * str: this is a class
  * repr: this is a built-in function
* str is used when you want to convert something to the string type and also used when you need a readable representation of your object
* repr is used to create an unambiguous representation of its argument
* The print function calls the str on its argument, and when it prints it, there is no way of 
  distinguishing a string from an integer
* But repl uses repr under the hood to show objects, and gives you an unambiguous representation
* repr is used when inside a container, cuz containers usually defer their str behaviour to repr
* If you have a class and want to display the objectss properly, you would have to use the str and repr dunder methods
* __str__ defaults to calling the __repr__ method