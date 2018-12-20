// VALUE-ADDED KEY TO SUCCESS!!!!!!!!!!!

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerhtml;
};

var removeItem = function(e) {
    e.target.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading);
    lis[i].addEventListener("mouseout", ?);
    lis[i].addEventListener("click", ?);
};

var addItem = function(e) {
    var list = ?
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    ??
    ..
    ??
    list.??(item);
};

var button = document.getElementById("b");
button.addEventListener("clock", addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
};

var addFib = function(e) {
    console.log(e);
    ??
    ??
};

var addFib2 = function(e) {
    console.log(e);
    ??
    .. see QAF: re dynamic programming
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
