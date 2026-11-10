from initialization import VDD

BIAS = -0.01   # Vset - Vmeasure，按实测修正

# Vout = 2.662 - 0.98*Vset  （2026-11-01 实测拟合）
def vset_to_dac_code(vset, bias=BIAS, vdd=VDD):
    v = vset + bias
    code = (2.662 - v) / 0.98 * 4095 / vdd
    return max(0, min(4095, round(code)))