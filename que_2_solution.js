

// Question 2.
// In JavaScript, answer if the following expressions result in true or false (and explain your
// answer)
// a. “0” == 0 // true or false?
// b. “” == 0 // true or false?
// c. “” == “0” // true or false?

a. “0” == 0 - TRUE // When we use '==', JavaScript will try to convert the expression we are trying to compare to same type.
//This can be overridden by using '===''

b. “” == 0 - TRUE //Reason for above example applies here too. The left operand is a string type and the right
//one is a number type for which JS will convert them to same type. In this case JS converts left operand to 
//number so number("") is 0. Thus 0 == 0.

c. “” == “0” -  FALSE //Left operand is an empty string which cannot be compared to a right operand string.
//Both LHS and RHS are of string types of which the left operand is empty but not right.