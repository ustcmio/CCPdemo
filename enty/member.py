
class Member(object):
    def __init__(self, name='', sfzh='', dybh='000', sex='', mz='', xl='', rylb='',szzb='', dnzw='', dfjz='', dylb='', rdrq='', zzrq='', jtdz='', lxfs='',
                 sjhm='', gzdw='', djzt='', sfsl='', sfld=''):
        self.name = name
        self.sex = sex
        self.mz = mz
        self.csrq = ''
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
        self.lxfs = lxfs
        self.sjhm = sjhm
        self.gzdw = gzdw
        self.djzt = djzt
        self.sfsl = sfsl
        self.sfld = sfld
        self.history = []

    def getName(self):
        return self.name

    def getSFZH(self):
        return self.sfzh

    def getUid(self):
        return self.dybh

    def getDYBH(self):
        return self.dybh

    def save(self,row):
        self.name = row[1]
        self.szzb = row[2]
        self.sfzh = row[3]
        self.sex = row[4]
        # if len(self.sfzh) == 18:
        #     s = self.sfzh[16]
        #     if s%2 ==0:
        #         self.sex = '女'
        #     if s%2 == 1:
        #         self.sex = '男'
        self.mz = row[5]
        self.csrq = row[6]
        self.xl = row[7].split(' ')[1]
        self.dylb = row[8]
        self.rdrq = row[9]
        self.zzrq = row[10]
        self.rylb = row[11]
        self.lxfs = row[13]
        self.sjhm = row[12]
        self.jtdz = row[14]
        # self.dybh = dybh
        # self.dnzw = dnzw
        # self.dfjz = dfjz
        # self.gzdw = gzdw
        self.djzt = row[15]
        self.sfsl = row[16]
        self.slrq = row[17]
        self.sfld = row[18]
        self.ldqx = row[19]

    def addHistory(self, record):
        self.history.append(record)

    def getInfo(self):
        if self.sjhm:
            lxfs = self.sjhm
        else:
            lxfs = self.lxfs
        return [self.dybh,self.szzb,self.dylb,self.name,self.sex,self.sfzh,self.jtdz,lxfs,self.dfjz,self.dnzw]

    def getInfoPro(self):
        return None
