var path = require("path");
console.log("normalization: "+path.normalize('D:/Pasha//NodeJS'));
console.log("joint path: "+path.join('D:/Pasha//NodeJS','/NewPath'));
console.log("resolve: "+path.resolve('path.js'));
console.log("ext name: "+path.extname('path.js'));