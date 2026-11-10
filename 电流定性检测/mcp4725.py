class MCP4725:
    def __init__(self, i2c, addr=0x60):
        self.i2c = i2c
        self.addr = addr

    def set_dac(self, dac_val):
        dac_val = max(0, min(4095, int(dac_val)))
        high = (dac_val >> 8) & 0x0F      # 快速写命令，高4位为0
        low  = dac_val & 0xFF
        self.i2c.writeto(self.addr, bytearray([high, low]))

    def set_voltage(self, v, vdd):
        """按目标电压换算 code 并输出"""
        code = int(4095 * v / vdd)
        self.set_dac(code)
        return code