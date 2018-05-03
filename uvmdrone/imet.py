import serial


def capture_imet_port(port,ser):
    """ Attempt to open Imet sensor port

    Parameters
    ------------
    port: string
        Port in system where Imet sensor is mounted eg /dev/ttyUSB0

    Return
    ------
    ser: serial.serialposix.Serial
    """
    ser = None
    try:
        ser = serial.Serial(port, baudrate=57600)

    except serial.SerialException as e:
        pass
    return ser


def stream_imet (ser, control=0):
    """ Capture stream of data from an Imet sensor USB serial port
    
    Parameters
    ----------
    ser: serial.serialposix.Serial
    control: int
        integer used to control the stream
        Default set to 0, capturing will continue until changed

   """
    # TODO  Change output to a ROS2 stream
    if ser == None:
        exit(1)

    while control==0:
        line = ser.readline()
        return line



