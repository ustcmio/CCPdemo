import xlrd
import datetime

class Member(object):
    def __init__(self, name='', sfzh='', dybh='', sex='', mz='', xl='', rylb='',szzb='', dnzw='', dfjz='', dylb='', rdrq='', zzrq='', jtdz='', lxfs='',
                 sjhm='', gzdw='', djzt='', sfsl='', sfld='', slrq ='', wclx = '', bz =''):
        # 姓名
        self.name = name
        # 性别
        self.sex = sex
        # 民族
        self.mz = mz
        # 出生年月
        self.csrq = ''
        # 学历
        self.xl = xl
        # 身份证号
        self.sfzh = sfzh
        # 人员类别
        self.rylb = rylb
        # 党员编号
        self.dybh = dybh
        # 所在支部
        self.szzb = szzb
        # 党内职务
        self.dnzw = dnzw
        # 党费交至
        self.dfjz = dfjz
        # 党员类别
        self.dylb = dylb
        # 入党日期
        self.rdrq = rdrq
        # 转正日期
        self.zzrq = zzrq
        # 家庭地址
        self.jtdz = jtdz
        # 联系方式（座机）
        self.lxfs = lxfs
        # 手机号码
        self.sjhm = sjhm
        # 工作单位
        self.gzdw = gzdw
        # 党籍状态
        self.djzt = djzt
        # 是否失联
        self.sfsl = sfsl
        # 失联日期
        self.slrq = slrq
        # 是否流动
        self.sfld = sfld
        # 外出流向
        self.wclx = wclx
        # 备注
        self.bz= bz
        self.history = []


    def save(self,row):
        self.name = row[1]
        self.szzb = row[2]
        self.sfzh = row[3]
        self.sex = row[4]
        self.mz = row[5].split(' ')[1]
        self.csrq = self.timeformat(row[6])
        self.xl = row[7].split(' ')[1]
        self.dylb = row[8]
        self.rdrq = self.timeformat(row[9])
        self.zzrq = self.timeformat(row[10])
        self.rylb = row[11].split(' ')[1]
        self.lxfs = row[13]
        self.sjhm = str(row[12]).split('.')[0]
        self.jtdz = row[14]
        self.dybh = row[20]
        self.dnzw = row[21]
        self.dfjz = row[22]
        self.gzdw = row[23]
        self.bz = row[24]
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
        return [self.dybh,self.szzb,self.dylb,self.name,self.sex,self.sfzh,self.jtdz,lxfs,self.dnzw]

    def getInfoPro(self):
        return None

    # 日期转换函数
    def timeformat(self, time):
        if time:
            if isinstance(time, float):
                return xlrd.xldate_as_datetime(time,0)
            if isinstance(time, str):
                return datetime.datetime.strptime(time,'%Y-%m-%d')
        else:
            return ''

    def getDYBH(self):
        return self.dybh