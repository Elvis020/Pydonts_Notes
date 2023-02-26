# Chaining Comparing Operators
* In python `a<b<c` b gets evaluated once, whiles with `a<b and b<c` b gets evaluated twice
* Also, basically in Python you can chain an arbitrary number of operators
* Note that although `a==b==c` is valid, and it's used to check if a,b and c are equal, `a != b != 
  c` is invalid because the `!=` operator is non-transitive
* When using `a<b and b<c`, note that if b has side effects, or it is non-constants, it won't work
* Note that `a < b > c` is the same as `b > max(a,c)`
* Chaining comparison operators feels natural but some chains may throw you off, if you overlook 
  them