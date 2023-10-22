import decimal
class converter:
    def __init__(self, volt,maxvolt,minvolt,numbits):
        self.maxvolt=5
        self.minvolt=0
        if(volt>=minvolt and volt<=maxvolt):
            self.volt=volt
        self.numbits=10
    def ToDigital(self):
        return bin(round(self.volt/5*1023))
    def SetDigitalValue(self,value):
        if(len(str(value))<self.numbits):
            dec=decimal.Decimal(value)
            myvolt=dec/1023*5
            self.volt=myvolt