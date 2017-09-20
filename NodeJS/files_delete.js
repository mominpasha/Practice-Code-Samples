var fs = require("fs");
fs.unlink("input.txt",function(err){
	if(err){
		return console.error(err);
	}
	console.log("FIle Deleted");
});