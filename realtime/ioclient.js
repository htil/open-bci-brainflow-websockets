class IOClient {
  socket = undefined;

  constructor(address) {
    console.log("IOClient init.");
    this.socket = io(address);
  }

  on(msg, handler) {
    this.socket.on(msg, handler);
  }

  send(msg, data) {
    this.socket.emit(msg, { data: data });
  }

  disconnect() {
    this.socket.disconnect();
  }
}
