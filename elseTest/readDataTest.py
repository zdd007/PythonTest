import xlrd
class ExcelUtil():
    def __init__(self,excelpath, sheetName):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetName)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
        # 获取table的第一行作为key值
        self.keys = self.table.row_values(0)
    def dict_excel(self):
        if self.nrows <= 1:
            print("总行数小于1")
        else:
            # 定义列表r
            r = []
            j = 1
            for i in range(self.nrows - 1):
                '''
                在总行数范围里面执行循环
                '''
                # 定义字典s
                s = {}
                values = self.table.row_values(j)#获取第二行的数据值
                for x in range(self.ncols):
                    '''
                    在列范围里面循环
                    '''
                    s[self.keys[x]] = values[x]#将value列表中的中通过x下标取出来，然后赋给字典s的key键对应的值
                r.append(s)#把S
                j+=1
            return r
if __name__ == "__main__":
        excelpath = "F:\PythonTest\excel.xlsx"
        sheetName = "user"
        data = ExcelUtil(excelpath, sheetName)
        print(data.nrows)
        print(data.ncols)
        print(data.dict_excel())





