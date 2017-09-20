//import events module
var events = require('events');
//create an event emitter object
var eventEmitter = new events.EventEmitter();
var connectHandler = function connected() {
	console.log("Connection Successful");
	eventEmitter.emit('data_received');
}
eventEmitter.on('connection',connectHandler);
eventEmitter.on('data_received',function(){
	console.log("data received successfully");
});
eventEmitter.emit('connection');
console.log("Program ended");