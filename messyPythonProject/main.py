import machine
import utime
import ustruct

# I2C setup for GPS (PA1010D)
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)  # 400kHz I2C frequency
GPS_I2C_ADDRESS = 0x10  # Default I2C address of PA1010D

# UART setup for XBee communication
xbee_uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

def read_nmea():
    """Reads NMEA sentences from the PA1010D GPS via I2C."""
    try:
        # Read up to 255 bytes of data from GPS
        data = i2c.readfrom(GPS_I2C_ADDRESS, 255)
        # Decode and split data by line breaks
        nmea_sentences = data.decode('utf-8').split("\r\n")
        return nmea_sentences
    except Exception as e:
        print(f"Aiya there is an error reading from GPS: {e}")
        return []

def parse_nmea(sentence):
    """Parses NMEA sentence and extracts relevant GPS data."""
    try:
        if sentence.startswith("$GPGGA"):  # Global Positioning System Fix Data
            data = sentence.split(",")
            time_utc = data[1]
            latitude = float(data[2]) if data[2] else 0.0
            lat_dir = data[3] if data[3] else ""
            longitude = float(data[4]) if data[4] else 0.0
            lon_dir = data[5] if data[5] else ""
            fix_status = data[6]
            num_satellites = int(data[7]) if data[7] else 0
            altitude = float(data[9]) if data[9] else 0.0

            # Return all relevant GPS data
            return time_utc, latitude, lat_dir, longitude, lon_dir, fix_status, num_satellites, altitude
    except IndexError:
        print("Malformed NMEA sentence wor ho ci!")
    return "", 0.0, "", 0.0, "", "", 0, 0.0

def send_message(message):
    """Send a message via the XBee module."""
    xbee_uart.write(message + "\r\n")  # Append a newline for easy parsing
    print(f"Sent jor: {message}")

while True:
    # Read and parse NMEA data from GPS
    nmea_sentences = read_nmea()
    gps_data = None
    for sentence in nmea_sentences:
        print(f"Raw NMEA hai gum yeung geh: {sentence}")
        gps_data = parse_nmea(sentence)
        if gps_data[1] != 0.0:  # If valid GPS data is found
            break

    # If valid GPS data was found, extract and process it
    if gps_data:
        time_utc, latitude, lat_dir, longitude, lon_dir, fix_status, num_satellites, altitude = gps_data

        # Pack all the GPS data into a binary format using ustruct
        packed_data = ustruct.pack(
            '10sff10s10siii',  # Format: 10-byte string (time), 2 floats (latitude/longitude), 2 strings (lat_dir/lon_dir), 3 ints (fix_status, num_satellites, altitude)
            time_utc.encode('utf-8'),
            latitude, longitude, lat_dir.encode('utf-8'), lon_dir.encode('utf-8'),
            int(fix_status), num_satellites, int(altitude)
        )

        # Send the packed binary data via XBee
        send_message(packed_data)

    # Wait for 2 seconds before the next iteration
    utime.sleep(2)
