var fs = require("fs");
var buf = new Buffer(1024);
console.log("Going to open an existing file");
fs.open("input.txt","r+",function(err,fd){
	if(err){
		return console.error(err);
	}
	fs.read(fd,buf,0,buf.length,0,function(err,bytes){
	if(err){
		return console.error(err);
	}
		console.log(bytes+" bytes read");
		fs.truncate(fd,10,function(err){
				if(err){
		return console.error(err);
	}
		});
		fs.close(fd,function(err){
			if(err){
		return console.error(err);
	}
			
		});
	});
});