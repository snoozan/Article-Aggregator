//<script type="text/javascript" src="scraper.php"></script>
//var tempJSONList = row_to_json(row(1,'foo'));

//document.getElementById("demo").innerHTML = (tempJSONList);
var testVar = [{"url": ["http://jvns.ca/blog/2014/04/26/i-dont-feel-guilty-about-not-contributing-to-open-source/"], "title": ["Don't feel guilty about not contributing to open source"]},
	{"url": ["http://rustbyexample.github.io/"], "title": ["Rust by Example"]},
	{"url": ["https://vimeo.com/85490944"], "title": ["Spotify Engineering Culture - part 1"]},
	{"url": ["http://forum.lazarus.freepascal.org/index.php/topic,24351.0.html"], "title": ["Lazarus Free Pascal IDE 1.2.2 is released and built with fpc 2.6.4"]},
	{"url": ["http://www.haskellforall.com/2014/04/model-view-controller-haskell-style.html"], "title": ["Type Safe MVC in Haskell"]},
	{"url": ["http://daniel.haxx.se/http2/"], "title": ["HTTP2 Explained"]},
	{"url": ["https://medium.com/the-physics-arxiv-blog/2c567adbf7fc"], "title": ["The Face Recognition Algorithm That Finally Outperforms Humans"]},
	{"url": ["https://www.kickstarter.com/projects/guardyen/metawear-production-ready-wearables-in-30-minutes"], "title": ["Build a Smart Bluetooth device in 30 minutes or less with hardware that runs Objective-C or Java"]},
	{"url": ["http://www.acomar.net/posts/2014-04-25-Foreign-CPP-Useful-Types-For-CPP-Interop.html"], "title": ["Accessing standard C++ types in Haskell"]},
	{"url": ["http://blogs.msdn.com/b/oldnewthing/archive/2014/04/25/10520321.aspx"], "title": ["A discovered quirk is just few steps away from becoming a feature"]},
	{"url": ["https://www.youtube.com/watch?v=yFIa-Mc2KSk"], "title": ["Devs and Depression by Greg Baugues"]},
	{"url": ["http://julien.danjou.info/blog/2014/a-b-testing-with-apache"], "title": ["Doing A/B testing with Apache httpd"]},
	{"url": ["http://journal.stuffwithstuff.com/2014/04/22/zero-to-95688-how-i-wrote-game-programming-patterns/"], "title": ["Zero to 95,688: How I wrote Game Programming Patterns"]},
	{"url": ["http://spage.fi/software-fail"], "title": ["Why do software projects fail?"]},
	{"url": ["http://www.washingtonpost.com/blogs/the-switch/wp/2014/04/24/64000-software-engineers-have-settled-with-tech-companies-over-wage-collusion/"], "title": ["64,000 software engineers have settled with tech companies over wage collusion"]},
	{"url": ["https://github.com/nikswamy/FStar"], "title": ["F* (a dependently-typed variant of F# for program verification) re-released under Apache 2.0"]},
	{"url": ["http://blog.gatunka.com/2014/04/25/character-encodings-for-modern-programmers/"], "title": ["ASCII and Unicode, Linux and Windows, and Programming"]},
	{"url": ["http://www.toptal.com/c-sharp/top-10-mistakes-that-c-sharp-programmers-make"], "title": ["Top 10 Mistakes that C# Programmers Make"]},
	{"url": ["http://joshrendek.com/2014/04/motivation-to-work-on-new-projects/"], "title": ["Motivation to work on new projects"]},
	{"url": ["http://stevemostovoy.com/portfolio/web-symphony/"], "title": ["WebSymphony - How to turn any website into an animated song"]},
	{"url": ["http://en.docsity.com/news/programming-2/free-libraries-for-everyday-work-in-popular-languages/"], "title": ["Free useful Libraries for everyday challenges in Popular Languages"]},
	{"url": ["http://jeremykun.com/2012/07/18/the-fast-fourier-transform/"], "title": ["The Fast Fourier Transform"]},
	{"url": ["http://www.infoworld.com/d/application-development/12-ethical-dilemmas-gnawing-developers-today-240574"], "title": ["12 ethical dilemmas gnawing at developers today"]},
	{"url": ["http://cppblogs.blogspot.com/2014/04/calling-conventions-is-very-important.html"], "title": ["Learn C++: Calling Conventions"]},
	{"url": ["http://youtu.be/nEm2eD4JfjE"], "title": ["Control your Arduino using C# windows form application."]}];


var articleHTML = "";

	
document.getElementById("slide1").innerHTML = (testVar[0].title);

//document.getElementById("slide1p").innerHTML = (testVar[0].summary);

document.getElementById("slide2").innerHTML = (testVar[1].title);

//document.getElementById("slide2p").innerHTML = (testVar[1].summary);

//document.getElememtById("slide3").innerHTML = (testVar[2].title);
//document.getElementById("slide3p").innerHTML = (testVar[2].summary);


for (var i=0; i < testVar.length; i += 1) {
	articleHTML = articleHTML.concat("<b>" + testVar[i].title + "<\/b><br>");
	//articleHTML = articleHTML.concat("&#09;" + testVar[i].summary + "<br>");
	articleHTML = articleHTML.concat("\<a class=\"btn btn-sm btn-primary\" href=\"" + testVar[i].url +"\" role=\"button\"\>Read More\<\/a\><br><br>");
}

	document.getElementById("articles").innerHTML = (articleHTML);
//document.write(testVar);


