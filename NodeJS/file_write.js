var fs = require("fs");
//Async way
fs.writeFile("input.txt","Simply Learning",function(err){
	if(err){
		return console.error(err);
	}
fs.readFile("input.txt",function(err,data){
	if(err){
		return console.error(err);
	}
	console.log("Read: "+data.toString());
});	
});
