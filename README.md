# CodeKataTrinaryLogic
## Background
Three-valued logic is a multiple-valued logic system in which there are three truth values; for this kata they will be True, False and Unknown. In this kata, T stands for True, F stands for False and U stands for Unknown. They are also represented as 1, -1 and 0 respectively.

This is the basic truth table:
<pre>
*---+---+-------+---------+--------+---------*
| P | Q | not P | P and Q | P or Q | P xor Q |
| T | T |   F   |    T    |   T    |    F    |
| T | U |   F   |    U    |   T    |    U    |
| T | F |   F   |    F    |   T    |    T    |
| U | T |   U   |    U    |   T    |    U    |
| U | U |   U   |    U    |   U    |    U    |
| U | F |   U   |    F    |   U    |    U    |
| F | T |   T   |    F    |   T    |    T    |
| F | U |   T   |    F    |   U    |    U    |
| F | F |   T   |    F    |   F    |    F    |
*---+---+-------+---------+--------+---------*
</pre>
Commutativity holds in this three-valued logic.

For example:

T and U  is equal to  U and T.

In general:
p and q  is equal to  q and p.
Moreover, for identical operators, associativity holds in this three-valued logic.

For example:

`(U or T) or F  is equal to  U or (T or F).`
<pre>
((T xor F) xor U) xor T  is equal to
  (T xor (F xor U)) xor T,
  T xor ((F xor U) xor T), 
  T xor (F xor (U xor T)),
  (T xor F) xor (U xor T).
</pre>
Note that the law of the excluded middle and the law of non-contradiction do not hold in this three-valued logic.

For example:
<pre>
U and not U  is not equal to  F.
not U or U  is not equal to  T.
</pre>
Read more about three-valued logic on Wikipedia.

Task
Write a function threevl that accepts an expression ( as a string ) and returns its value ( as 1, 0, or -1 ).

For example:
<pre>
"not T or U"             ->  0
"not (T or U)"           -> -1
"U and not U"            ->  0
"not (F and (U xor T))"  ->  1
</pre>
Notes
Always evaluate expressions inside brackets first.
This kata only uses 4 operators not, and, xor, or.
Their priorities, from highest to lowest, are: not, and, xor, or. Hence, not T or F xor U should equal (not T) or (F xor U).
Input
0 <= the number of operators < 59
There will be no invalid inputs.
There are 300 random tests. Good luck and happy coding!
