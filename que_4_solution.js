// Question 4.
function weird(x) {
	var tmp = 3;
	return function(y) {
		return x + y + ++tmp;
	}
}
var funny = weird(2);
var final_answer = funny(10);

console.log(final_answer)
// What is the value of final_answer at the end of this snippet? : 16

//Please explain your answer:

//Explanation

/*Variable called funny is actually a function where you have passed in 10, but the initial weird passes 
in 2 and tmp = 3 but ++tmp = (3+1) = 4 so the result when you pull the final answer is 10+2+4 = 16*/