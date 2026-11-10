import time

class ADS1115:
    _MUX = [0b100, 0b101, 0b110, 0b111]
    _FS  = [6.144, 4.096, 2.048, 1.024, 0.512]

    def __init__(self, i2c, addr=0x48):
        self.i2c = i2c
        self.addr = addr

    def read_voltage(self, channel=0, pga=1):
        mux = self._MUX[channel]
        cfg = (1 << 15) | (mux << 12) | (pga << 9) | (0 << 8) | (0b100 << 5) | 0x0003
        self.i2c.writeto_mem(self.addr, 0x01, bytearray([(cfg >> 8) & 0xFF, cfg & 0xFF]))
        time.sleep_ms(15)                       # 等待转换完成
        buf = self.i2c.readfrom_mem(self.addr, 0x00, 2)
        raw = (buf[0] << 8) | buf[1]
        if raw >= 0x8000:
            raw -= 65536
        return raw * self._FS[pga] / 32768.0