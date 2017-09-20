var buffer1 = new Buffer('Buffer1');
var buffer2 = new Buffer('Buffer2');
var buffer3 = Buffer.concat([buffer1,buffer2]);

console.log(buffer3.toString());
