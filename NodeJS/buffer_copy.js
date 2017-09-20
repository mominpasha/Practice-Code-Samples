var buffer1 = new Buffer('abcdefghijklmnop');
var buffer2 = new Buffer(16);
buffer1.copy(buffer2);
console.log(" Buffer 2 content: " + buffer2.toString());
console.log(" Buffer 1 Slice: " + buffer1.slice(0,9));