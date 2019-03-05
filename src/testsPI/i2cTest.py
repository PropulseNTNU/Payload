# Register addresses (with "normal mode" power-down bits)
reg_write_dac = 0x40

# Initialize I2C
bus = smbus.SMBus(channel)

# Create a sawtooth wave 16 times
for i in range(0x10000):

    # Create our 12-bit number representing relative voltage
    voltage = i & 0xFFFF

    msg = (voltage & 0xFF0) >> 4
    msg = [msg, (msg & 0xF) << 4]

    bus.write_i2c_block_data(address, reg_write_dac, msg)