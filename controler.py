import os
import pickle
from datetime import datetime
from enty.member import Member

class Controller(object):
    def __init__(self):
        self.datafilename = 'database.pkl'
        self.data = []
        self.dataAll = {}
        self.dataIn = []
        self.dataOut = []
        self.initData()
        if self.data:
            self.dataAll, self.dataIn, self.dataOut = self.data
        pass

    # 初始化数据，从默认数据文件读取数据
    def initData(self):
        if os.path.exists(self.datafilename):
            with open(self.datafilename, 'rb') as f:
                self.data = pickle.load(f)
        else:
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
        self.dataAll[member.szzb].append(member)
        self.dataIn.append(member)

    # 删除党员
    def dele(self, member):
        self.dataAll[member.szzb].pop(member)
        self.dataOut.append(member)

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

    def getData(self, szzb):
        return sorted(self.dataAll[szzb],key=self.func)

    def getAllData(self):
        all = []
        for members in self.dataAll.values():
            all.extend(members)
        all.sort(key = self.func)
        return all


    def func(self,member):
        return member.dybh


if __name__ == '__main__':
    c = Controller()
    # c.add(Member('张三','111111111111111111','042030338',szzb='四支部'))
    # c.add(Member('李四', '111111111111111112', '042030339', szzb='二支部'))
    # c.add(Member('王五', '111111111111111113', '042030340', szzb='一支部'))
    # c.add(Member('赵六', '111111111111111114', '042030341', szzb='三支部'))
    # c.add(Member('陈七', '111111111111111115', '042030342', szzb='一支部'))
    # c.add(Member('朱六', '111111111111111116', '042030343', szzb='二支部'))
    # c.saveToDatabase()
    for member in c.getData('三支部'):
        print(member.name,member.szzb,member.dybh,member.sfzh)