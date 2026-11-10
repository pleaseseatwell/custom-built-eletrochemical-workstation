from machine import SoftI2C, Pin

I2C_FREQ = 100000
MCP4725_ADDR = 0x60
ADS1115_ADDR = 0x48
VDD = 3.47                     # 基准电压，统一在此维护

_i2c = None

def get_i2c(sda=16, scl=17, freq=I2C_FREQ):
    """单例：多次调用返回同一个 I2C 对象"""
    global _i2c
    if _i2c is None:
        _i2c = SoftI2C(sda=Pin(sda), scl=Pin(scl), freq=freq)
        
    return _i2c