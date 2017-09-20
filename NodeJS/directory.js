var fs = require("fs");
fs.mkdir("D:/Pasha/NodeJS/SampleFolder",function(err){
	if(err){
		return console.error(err);
	}
	console.log("Created Directory");
});
fs.readdir("D:/Pasha/NodeJS/",function(err,files){
	if(err){
		return console.error(err);
	}
	files.forEach(function(file){
		console.log(file);
	});
});
fs.rmdir("D:/Pasha/NodeJS/SampleFolder",function(err){
	if(err){
		return console.error(err);
	}
	console.log("Deleted Directory");
});
