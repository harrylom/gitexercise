import decimal
class converter:
    def __init__(self, volt):
        self.volt=volt
    def ToDigital(self):
        return bin(round(self.volt/5*1023))
    def SetDigitalValue(self,value):
        dec=decimal.Decimal(value)
        myvolt=dec/1023*5
        self.volt=myvolt