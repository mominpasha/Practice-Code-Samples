var os = require("os");
console.log("Endianness: "+os.endianness());
console.log("OS Type: "+os.type());
console.log("OS Platform: "+os.platform());
console.log("OS Total Memory: "+os.totalmem()+" bytes");
console.log("OS Free Memory: "+os.freemem()+" bytes");