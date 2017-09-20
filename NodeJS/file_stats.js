var fs = require("fs");
console.log("Going to get file info!");
fs.stat("input.txt",function(err,stst){
	if(err){
		return console.error(err);
	}
	console.log(stats);
	console.log("IsFile? "+ stats.isFile());
	console.log("IsDirectory? "+ stats.isDirectory());
});
