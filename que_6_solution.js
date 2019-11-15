//  Write a program (in Python, JavaScript or Ruby) to populate and then sort a
//  randomly distributed list of 1 million integers, each integer having a value >= 1 and <=
//  100 without using any builtin/external library/function for sorting.
//  Your program should carefully consider the input and come up with the most efficient
//  sorting solution you can think of. Provide the space and time complexity of your algorithm

//  Used JavaScript for below solution

//Create an Array and fill random integers in it, added 100 random integers between 1 to 100 instead of 1 million due to space.
var Numbers = [];
for (i = 1; i < 100; i++) { 
	/*Returns a random number between min (inclusive) and max (exclusive)
	return Math.random() * (max - min) + min;*/
	Numbers.push((parseInt((Math.random() * (100 - 1) + 1))));
}
console.log(Numbers.sort());




//  Linear Time — O(n)
//  An algorithm is said to have a linear time complexity when the running time increases at most 
//  linearly with the size of the input data. This is the best possible time complexity when the algorithm must 
//  examine all values in the input data