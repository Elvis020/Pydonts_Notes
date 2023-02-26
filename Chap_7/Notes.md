# Truthy, False and bool
* To check if an object is Truthy or Falsy, you can use `bool()` 
* The value of a given type is Falsy when it is 'empty' or 'without any useful value'
* An object can define it's bool() value by playing around with the `__bool__()`
* How python evaluate truthy or falsy
  * First it attempts to use the __bool__ method
  * If the __bool__ method is not implemented, then it tries to call `len()` on it
  * If that fails, den it defaults to giving it a Truthy value
* The bool of None is Falsy, so if you have a meaning value, use `value is None` or `value is not None` and not `if not value` and `if value`
* Situations where truthy and Falsy values are used
  * When processing input data, to check if there is data coming in or not