
from pyfirmata import Arduino, util
import time
board = Arduino('/dev/cu.usbmodem141221')

key = "tAsLon5bqbHdFNzca01BlkGeyCGGv9EX"
url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/boat.mp3"
service = "service"
reason = "reason"
message = "hello there"
vol = "25"


def button():
    it = util.Iterator(board)
    it.start()

    button = board.get_pin('d:2:i')
    light = board.get_pin('d:8:o')

    while True:
        if button.read() == 1:
            payload = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + vol + "</volume></play_info>"
            p = requests.post('http://192.168.1.72:8090/speaker', data=payload)
