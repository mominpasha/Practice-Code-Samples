var fs = require("fs");
var data = '';
var readerStream = fs.createReadStream("input.txt");
readerStream.setEncoding('UTF8');
readerStream.on('data',function(chunk){
	console.log('------Chunk:'+chunk);
	console.log(chunk.length)
	data+=chunk;
});
readerStream.on('end',function(){
	console.log(data);
});
readerStream.on('error',function(err){
	console.log(err.stack);
});

var data1 = "Output Data";
var writerStream = fs.createWriteStream("output.txt");
writerStream.write(data1,'UTF8');
writerStream.on('finish',function(){
	console.log("Write Complete");
});
writerStream.on('error',function(err){
	console.log(err.stack);
});
console.log("Program Ended");

readerStream.pipe(writerStream);