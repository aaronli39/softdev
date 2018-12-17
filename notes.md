```
 __   ___   ____ _____  ___   ____  _          _      ___  _____  ____  __
( (` / / \ | |_   | |  | | \ | |_  \ \  /     | |\ | / / \  | |  | |_  ( (`
_)_) \_\_/ |_|    |_|  |_|_/ |_|__  \_\/      |_| \| \_\_/  |_|  |_|__ _)_)
___________________________________________________________
 ___,                                _
/   |                             \_|_)  o
|    |   __,   ,_    __   _  _       |
|    |  /  |  /  |  /  \_/ |/ |     _|    |
 \__/\_/\_/|_/   |_/\__/   |  |_/  (/\___/|_/
___________________________________________________________
```

-----

# 12/17/18

**Aim:**: 90s BS - JS

**1995**: @NETSCAPE Communicatins
* Brendan Eich writes prototype of JS in 10 days
* the internet in the early days was a collection of hyperlinks
* JS created b/c the internet was in need of a scripting language
* scheme is a very robust language!
* the web is using heavily more functional programming languages

**BIG IDEA: Scheme + Java -> Javascript**
* lets give scheme the *syntax of Java* and mooch of Java's populatiry by calling this javascript
* **JS is not a light version of Java**, and has **no resemblance to Java**

**90's browser wars: IE vs Netscape**:
* Microsoft tried to dominate by packaging each Windows machine with a browser, as opposed to NetScape b/c one had to install it
* **1996:** VBscript/Jscript were MS's attempted implementations
* development was not uniform for IE vs other browsers(NETSCAPE)
* JS was *slow*

**Darci DiNucci(1999)**:
* had a vision of **Web 2.0**, which resembles today's internet.
* it will appear on your screen as a page of interactivity

**2005: JS goes mainstream**:
* advent of web 2.0(2 way comm)
* **Jesse James Garett**: wrote guides on JS-driven page updates w/o reload("asyncrhnous")

**JS features**:
* dynamic typing
* first-class fxns
    * can be treated like vars(pass, returned)
    * you can give a function a name and then pass around that function by name
* object-oriented(if you'd like, or an imperative lang)
* functional

*JS limitations*
* no I/O(networking, storage, graphics)

*JS syntax*:
* from C(like Java, Python, C++, etc)
* auto-semicolon-ination!(browser will assume and assert)

Best practices(**AVOID**):
```js
function fxnName(args) {
    body;
}
```
Instead **take advantage of first class fxns**, DO:
```js
var fxnName = function(args) {
    body;
};

// or

var fxnName = (args) => {
    body;
};
```

* easier to understand "fxn as obj"
    * can be reassigned
    * can be passed as an args
    * "lambda" <=> "function"
* enforces better semicolon habits

-----

# 12/14/18

**Aim**: What happened in the 1990s?

**DN**: Scheme definition of fact(n)?

* windows 3/0
* macintosh system 6(if u were cool)
* CERN: neXT machine(first heavy duty machine that scentists worked on)(collider)
* TB-L writes **worldwideweb**, first graphical web browser(WYSIWYG html editor)
* LaTeX - a markdown language

**1991**:

* Gore Bill passes. Why do we care?
* ```lynx```: a terminal www browser
    * oldest browser still in use.
    * faaaaaaaaaaaaaast(cus no images/ stuff)
    * malware impervious
    * allows cookies nowadays

**Java**:

* Java is in vogue
* **mosaic(UIUC)**: first mainstream graphical web browser bc:
    * windows port
    * supports multiple internet protocols(hence name)
        * FTP
        * Gopher
        * HTTP
        * etc
    * runs on windows instead of only on NeXT
    * images in line with text(instead of separate windows)

**1994, a super cool nerds window**

* slipknot web browser
* MOSAIC COmmunications founded in Mtn View
    * mosaic netscape offers similar UX as Mosaic
    * same team
    * different src
    * a16z?
* Mozilla is born!(internal codename: MOZaic kILLa)

-----

# 11/16/18

**Aim**:

-----

# 11/15/18

**Aim:** RESTed yet?

-----

# 11/14/18

**Aim:** Get more REST

```
u = request.urlopen(URL)
response = u.read()
data = json.loads(response) # save JSON obj as dictionary
return render_template("index.html", pic = data['url'])
```

**Why maintain API knowledge base?**
* lowers/refines the scope of existing APIs to narrow down to things that actually matter


-----

# 11/13/18

**Aim:** REST up

**API:** Application Program Interface

* published set of protocols that can be used to have your program interact with some other program/service
* examples:
    * Python API (Documentation)
    * Java API
    * Netlogo DOcumentation API
* not solely geared for programmers
* when we wrote an info tab for netlogo project, that is kind of an API
* declaring an interface in Java -> API
*
**REST:** **Re**presentative **S**tate **T**ransfer

* a REST API transmits data back after receiving an http(s) request
* returned data can be in various formats. Most common are HTML, XML, JSON
* often require a **key**(why?)
* we're gonna focus on JSON format
* read up on **Wikipedia** representative state transfer

**json** library facilitates ork with JSON data

* ```.loads()``` turns a JSON object string into a dictionary
* ```.dumps()``` turns python dict into JSON object string. EG: ```w = json.dumps(<DICTIONARY>)```

-----

# 11/08/18

**Aim:** REST up

**API:** Application Program Interface

* published set of protocols that can be used to have your program interact with some other program/service
* examples:
    * Python API (Documentation)
    * Java API
    * Netlogo DOcumentation API
* not solely geared for programmers
* when we wrote an info tab for netlogo project, that is kind of an API
* declaring an interface in Java -> API
*
**REST:** **Re**presentative **S**tate **T**ransfer

* a REST API transmits data back after receiving an http(s) request
* returned data can be in various formats. Most common are HTML, XML, JSON
* often require a **key**(why?)
* we're gonna focus on JSON format
* read up on **Wikipedia** representative state transfer

**json** library facilitates ork with JSON data

* ```.loads()``` turns a JSON object string into a dictionary
* ```.dumps()``` turns python dict into JSON object string. EG: ```w = json.dumps(<DICTIONARY>)```

-----

# 11/07/18
Task:

Be prepared to show and tell when you are visited
* 1 cool(CSS) thing your FEF can do

11/05/18
Aim: Bootstrap

Front-end frameworks:
-* foundation
-* Bootstrap

As a duo, look up either the bootstrap or foundation front end framework and:
* research framework
* create a single HTML page that demonstrates:
* the key features of your framework
* it should not be too complicated; you don't need to showcase EVERYTHING about the framework
* highlight the most attractive or useful features of your framework
* your page should provide a simpler on-ramp than the site

11/02/18
Cascading style sheets (css)
* created to separate presentation of an HTML/XML Page from its contents
* not limited to web pages(paper, etc)
* though HTML tags like <center* exist, you should henceforth avoid them
* 3 ways to style css:
* inline
* internal style sheet
* external style sheets

Basic syntax:
* Property: value;
Eg:
color: light blue;
border: 100px;

* Inline styling:
* syntax: <TAG stle="CSS CODE"*
eg: <p stle="color:green"*
* add CSS code to the style attribute of HTML tag
* good for trying things out
* .... but tedious if we want all of them to look the same, its tedious to
retype them over and over

* Internal Style sheets
* add a STYLE element to the section of the page
* include all CSS code inside the <style ... </style* block
* requires addition of a selector so that it is clear what element you are styling
* SYNTAX:
SELECTOR {
CSS CODE;
}
eg:
h1 {
color: #FF00FF; // this is purple(red + blue)
}

* External Style Sheets
* create a separate .css file that contains all of your CSS code
* it cannot contain any other kind of code(no HTML or XML)
* include a link to the CSS file inside the section of the HEAD section of your page
* SYNTAX:
eg:
<head*
<link rel="stylesheet" href="STYLE FILE" type="text/css"*
</head*

* GO GO WEB browser INSPECT!
* right click and select inspect
* interact with styles wihout having to touch them

* the DIV tag
... is a container element. Sole purpose is to define a section of your page that should be considered grouped together

* Class attribute
... is an identifier that can be applied to multiple elements. Any HTML element can have this.
eg:
<div class="navbar"* ... </div*
<h2 class="new_chapter"* ... </h2*

To access these classes in your CSS file, put a period in front of the class name:
eg:
.new_chapter {
text-align: center;
}
* ID Attributes
HTML elements can also have an ID attribute(identifier to be applied ONLY TO A SINGLE ELEMENT)
eg:
<div id="main_content"* ... </div*
To use a aselector in your CSS flies,
put a #(octothorp) in front of the ID tag
eg:
#main_content {
text-align: center;
}

* PROTIP:
you can use ID Names in tags as href target to jump around the same pages
eg:
<a href="#main_content"*... </a*

* Task: bookmarg:
developer.mozilla.org/en0US/docs/Web/CSS
(google MDN CSS)
___________________________________________________________________________
