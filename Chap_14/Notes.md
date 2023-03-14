# Structural pattern matching
* With match-case, each case must be followed by a pattern
* You case use the `__match_args__` to keep the code clean in the case of Point2D
* `*` or `**` can be used to match the remaining of a list or tuple
* Note that you can also do structural pattern matching on dictionaries
* In structural pattern matching, we can include dictionaries to prevent making the match-case 
  context long