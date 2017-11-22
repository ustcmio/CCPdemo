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
        # 最近转出党员
        self.dataOut = {}
        # 所有支部名称
        self.choices = []

        # 数据初始化，从数据库读取
        self.initData()

        if self.dataAll:
            self.choices = sorted(self.dataAll.keys(),key = self.func_sort_choices)

    # 清空数据库
    def clear(self):
        self.dataAll.clear()
        self.dataOut.clear()


    # 初始化数据，从默认数据文件读取数据，如果默认数据库不存在提示从备份文件读取或者导入Excel
    def initData(self):
        if os.path.exists(self.datafilename):
            with open(self.datafilename, 'rb') as f:
                data = pickle.load(f)
                if data:
                    self.dataAll, self.dataOut = data
        else:
            # 提示从备份文件读取或者导入Excel
            print("No database.pkl")

    # 保存到数据文件
    def savaData(self, filename):
        with open(filename, 'wb') as f:
             pickle.dump([self.dataAll,self.dataOut],f)

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

    # 由身份证号编号获取党员
    def getMemberByPID(self, pid):
        for members in self.dataAll.values():
            for member in members:
                if member.sfzh == pid:
                    return member
        return None

    def getAllData(self,szzb=None):
        if self.dataAll:
            if szzb:
                if szzb in self.dataAll.keys():
                    return self.dataAll[szzb]
            else:
                members = []
                for choice in self.choices:
                    members.extend(self.dataAll[choice])
                return sorted(members, key=lambda m: m.getDYBH())
        else:
            return None

    def getOutData(self):
        members = []
        for choice in self.dataOut.values():
            members.extend(choice)
        return sorted(members, key=lambda m: m.getDYBH())


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
        elif ext =='.xlsx':
            pass

    def getChoices(self):
        if self.dataAll:
            self.choices = sorted(self.dataAll.keys(),key = self.func_sort_choices)
        return self.choices

    def func_sort_choices(self,label):
        sorted_dict = {'一支部': 1, '二支部': 2, '三支部': 3, '四支部': 4, '五支部': 5, '六支部': 6, '七支部': 7, '八支部': 8 }
        for key in sorted_dict.keys():
            if key in label:
                print(sorted_dict[key])
                return sorted_dict[key]
        return 100

    def isEmpty(self):
        if self.dataAll:
            return True
        else:
            return False