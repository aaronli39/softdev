/*
Xiaojie(Aaron) Li, Ricky Lin, Team weWantJS
Softdev1 pd6
K28 -- Sequential Progression
2018-12-18
*/

var studentList = ["ricky", "aaron", "kyle", "kaitlin", "tim", "bo", "damian", "michelle"];

var fib = function(args) {
    if (args == 0) return 0;
    else if (args == 1) return 1;
    else {
        return fib(args - 1) + fib(args - 2);
    }
}

var gcd = function(num, denom) {
    var temp = num % denom;
    if (temp == 0) return denom;
    else return gcd(denom, temp);
}


var randStudent = function() {
    var len = studentList.length;
    var rand = Math.floor(Math.random() * len);
    // console.log(rand);
    return studentList[rand];
}

var display1 = function() {
    console.log(fib(10));
}
var display2 = function() {
    console.log(gcd(30, 40));
}
var display3 = function() {
    console.log(randStudent());
}

var fibbo = document.getElementsByClassName("fib");
fibbo.addEventListener('click', display1);
var gcdo = document.getElementsByClassName("gcd");
gcdo.addEventListener('click', display2);
var rando = document.getElementsByClassName("rand");
rando.addEventListener('click', display3);
