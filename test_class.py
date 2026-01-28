from calc.calculation import Zp


base_zp = Zp(oklad = 10000, isn = 0.1)
base_zp_kto = Zp(oklad = 10000, isn = 0.1)
zp_rop_kto = Zp(oklad = 10000, isn = 0.1, rop=0.4)
print(zp_rop_kto.zp_rop_kto())
