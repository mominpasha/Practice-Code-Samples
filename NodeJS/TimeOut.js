function helloWorld(){
	console.log("hello world");
}
var t = setTimeout(helloWorld,2000);
clearTimeout(t);

setInterval(helloWorld,2000);