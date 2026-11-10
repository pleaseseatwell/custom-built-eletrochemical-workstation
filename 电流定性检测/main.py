import gc
from initialization import get_i2c, VDD
from mcp4725 import MCP4725
from ads1115 import ADS1115
from calibration import vset_to_dac_code

def main():
    i2c = get_i2c()
    dac = MCP4725(i2c)
    adc = ADS1115(i2c)

    set_value = 0.2                      # 相对于 WE 的目标电压
    code = vset_to_dac_code(set_value)
    dac.set_dac(code)

    measured = adc.read_voltage(channel=0, pga=1)

    print("DAC代码 | 设定电压(V) | 实测电压(V)")
    print("-" * 36)
    print(f"{code:6d}  |   {set_value:.3f}    |   {measured:.3f}")

    dac.set_dac(0)
    gc.collect()

if __name__ == "__main__":
    main()