
class Zp:
    def __init__(self, oklad, isn, rop=0, kto = 0.3):
        self.oklad = oklad
        self.rop = rop * oklad
        self.isn = isn * oklad
        self.kto = (oklad + isn)*kto

    def base_zp(self):
        base_zp = self.oklad + self.isn
        base_zp = base_zp - base_zp*0.14
        return round(base_zp, 2)

    def base_zp_kto(self):
        base_zp_kto = self.oklad + self.isn + self.kto
        base_zp_kto = base_zp_kto - (base_zp_kto*0.14)
        return round(base_zp_kto, 2)

    def zp_rop_kto(self):
        zp_rop_kto = self.oklad + self.isn + self.rop + self.kto
        zp_rop_kto = zp_rop_kto - (zp_rop_kto * 0.14)
        return round(zp_rop_kto, 2)