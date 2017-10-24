import uuid


class Member(object):
    def __init__(self, name, sfzh, dybh, sex='', mz='', xl='', rylb='',szzb='', dnzw='', dfjz='', dylb='', rdrq='', zzrq='', jtdz='', lzfs='',
                 sjhm='', gzdw='', djzt='', sfsl='', sfld=''):

        self.name = name
        self.sex = sex
        self.mz = mz
        self.xl = xl
        self.sfzh = sfzh
        self.rylb = rylb
        self.dybh = dybh
        self.szzb = szzb
        self.dnzw = dnzw
        self.dfjz = dfjz
        self.dylb = dylb
        self.rdrq = rdrq
        self.zzrq = zzrq
        self.jtdz = jtdz
        self.lzfs = lzfs
        self.sjhm = sjhm
        self.gzdw = gzdw
        self.djzt = djzt
        self.sfsl = sfsl
        self.sfld = sfld
        self.history = []
        self.uid = uuid.uuid1()

    def getName(self):
        return self.name

    def getSFZH(self):
        return self.sfzh

    def getUid(self):
        return self.dybh

    def getDYBH(self):
        return self.dybh

    def save(self,name, sfzh, dybh, sex='', mz='', xl='', rylb='',szzb='', dnzw='', dfjz='', dylb='', rdrq='', zzrq='', jtdz='', lzfs='',
                 sjhm='', gzdw='', djzt='', sfsl='', sfld='',history = []):
        self.name = name
        self.sex = sex
        self.mz = mz
        self.xl = xl
        self.sfzh = sfzh
        self.rylb = rylb
        self.dybh = dybh
        self.szzb = szzb
        self.dnzw = dnzw
        self.dfjz = dfjz
        self.dylb = dylb
        self.rdrq = rdrq
        self.zzrq = zzrq
        self.jtdz = jtdz
        self.lzfs = lzfs
        self.sjhm = sjhm
        self.gzdw = gzdw
        self.djzt = djzt
        self.sfsl = sfsl
        self.sfld = sfld
        self.history = history

    def addHistory(self, record):
        self.history.append(record)

    def getInfo(self):
        return [self.dybh,self.szzb,self.dylb,self.name,self.sex,self.sfzh,self.jtdz,self.lzfs,self.sjhm,self.dfjz,self.dnzw]

    def getInfoPro(self):
        return None

