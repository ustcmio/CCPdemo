import os
import pickle
from datetime import datetime
import xlrd
from enty.member import Member

class Controller(object):
    def __init__(self):
        self.datafilename = 'database.pkl'
        # 保存所有党员，以支部为key
        self.dataAll = {}
        # 保存最近转入党员
        self.dataIn = {}
        # 最近转出党员
        self.dataOut = {}

        # 数据初始化，从数据库读取
        self.initData()

    # 清空数据库
    def clear(self):
        self.dataAll.clear()
        self.dataIn.clear()
        self.dataOut.clear()


    # 初始化数据，从默认数据文件读取数据，如果默认数据库不存在提示从备份文件读取或者导入Excel
    def initData(self):
        if os.path.exists(self.datafilename):
            with open(self.datafilename, 'rb') as f:
                data = pickle.load(f)
                if data:
                    self.dataAll, self.dataIn, self.dataOut = data
        else:
            # 提示从备份文件读取或者导入Excel
            print("No database.pkl")

    # 保存到数据文件
    def savaData(self, filename):
        with open(filename, 'wb') as f:
             pickle.dump([self.dataAll,self.dataIn,self.dataOut],f)

    # 默认自动保存到数据文件
    def saveToDatabase(self):
        self.savaData(self.datafilename)

    # 手动备份文件到bak
    def saveToBak(self):
        now = datetime.now()
        filename = 'database' + now.strftime("%Y%m%d%H%M%S") + '.bak'
        self.savaData(filename)

    # 新增党员
    def add(self, member):
        if member.szzb not in self.dataAll.keys():
            self.dataAll[member.szzb] = []
            self.dataIn[member.szzb] = []
        self.dataAll[member.szzb].append(member)
        self.dataIn[member.szzb].append(member)

    # 删除党员
    def dele(self, member):
        self.dataAll[member.szzb].pop(member)
        if member.szzb not in self.dataOut.keys():
            self.dataOut[member.szzb] = []
        self.dataOut[member.szzb].append(member)

    # 修改党员
    def change(self, old, new):
        pass

    # 查询党员
    def search(self, key=None):
        result = []
        for members in self.dataAll.values():
            for member in members:
                if member.name == key or member.sfzh == key :
                    result.append(member)
        return result

    # 由党员编号获取党员
    def getMemberByDYBH(self, dybh):
        for members in self.dataAll.values():
            for member in members:
                if str(int(member.dybh)) == dybh:
                    return member
        return None

    def getAllData(self):
        return self.dataAll

    def getInData(self):
        return self.dataIn

    def getOutData(self):
        return self.dataOut

    def getAllDataBySSZB(self,szzb):
        return {szzb: self.dataAll[szzb] }

    def getInDataBySSZB(self,szzb):
        return {szzb: self.dataIn[szzb] }

    def getOutDataBySSZB(self,szzb):
        return {szzb: self.dataOut[szzb] }


    # 从excel导入数据
    def dataFromExcel(self, filename):
        self.clear()
        ext = os.path.splitext(filename)[1]
        if ext == '.xls':
            workbook = xlrd.open_workbook(filename)
            sheet = workbook.sheet_by_index(0)
            # row = sheet.row_values(4)
            # print(row)

            for index in range(4,sheet.nrows):
                row = sheet.row_values(index)
                if row[3] and len(row[3])==18:
                    # print(row[0])
                    m = Member()
                    m.save(row)
                    self.add(m)
            pass
        elif ext =='.xlsx':
            pass

