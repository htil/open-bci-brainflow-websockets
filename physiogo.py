from acquisition import DataAcquisition
from physiodatastream import Streams
from realtime.ioserver import IOServer
import time
import atexit
import threading


# try making physiogo QT element
# Note make python a client that sends to a node server which echos messages to web?

def set_interval(func, sec):
    def func_wrapper():
        #set_interval(func, sec)
        while True:
            func()
            time.sleep(0.5)
    t = threading.Thread(target=func_wrapper)
    t.start()
    return t


class PhysioGo:
    def __init__(self, sensor_port, sensor_name, buffer_size=1000):
        self.boards = {"ganglion": 1}

        # Sensor
        self.sensor = DataAcquisition(sensor_port,  self.boards[sensor_name])
        self.sensor.startStreaming()
        self.channels = self.sensor.getChannels()
        self.streams = Streams(self.channels, buffer_size)
        self.sfreq = self.sensor.getSamplingRate()
        self.board = self.sensor.getBoard()

        # Socket
        self.socket = IOServer()
        self.socket.on("connect", self.onConnect)
        self.socket.on("stream", self.start)

        # Start Socket
        self.socket.runDaemon()

        set_interval(self.update, 1)

        # Cleanup Callback
        atexit.register(self.close)

        k = input("press c to exit")

    def onConnect(self):
        print('New Socket Connected')

    def close(self):
        self.sensor.end()
        print('Done')

    def update(self):
        print("update")
        self.socket.send('raw', "blah")
        #k = input("press c to exit")

    def start(self, msg):
        set_interval(self.update, 1)

        # Start Timer
        # self.timer.start()
        # while True:
        #    time.sleep(10)
        #    self.socket.send('raw', "blah")

        #data = self.sensor.getAllData()
        #self.socket.send('raw', data.tolist())
        #data = self.sensor.getAllData()
        #self.socket.send('raw', data.tolist())
