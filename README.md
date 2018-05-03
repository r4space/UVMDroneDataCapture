# Imet Serial port specs:
$ miniterm.py /dev/ttyUSB0  57600 --parity=N
Baud: 57600
Parity: None
Data Bits: 8 bits
Stop Bits: 1 bit 
Hardware Flow Control: None
Parameter positions:
XQ, Pressure, Temperature, Humidity, Date, Time, Latitude x 1000000, Longitude x 1000000, Altitude x
1000, Sat Count

# Docs
To rebuild docs:
$ make html
