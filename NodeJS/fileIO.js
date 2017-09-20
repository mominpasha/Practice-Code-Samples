var fs = require("fs");
//Async way
fs.readFile("input.txt",function(err,data){
	if(err){
		return console.error(err);
	}
	console.log("Asunc Read: "+data.toString());
});
//Sync Read
var data = fs.readFileSync('input.txt');
console.log(data.toString());