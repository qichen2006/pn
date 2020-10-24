# -*- coding: utf-8 -*-
# @Time : 2020/10/20 22:06

import xlrd
from common.public import filePath, readContent
from utils.operationYaml import OperationYaml


class ExcelValues(object):



    caseID = 0
    des = 1
    url = 2
    method = 3
    data = 4
    expect = 5

    @property
    def getcaseID(self):
        return self.caseID

    @property
    def getdescription(self):
        return self.des

    @property
    def geturl(self):
        return self.url

    @property
    def getmethod(self):
        return self.method

    @property
    def getdata(self):
        return self.data

    @property
    def getexpect(self):
        return self.expect


class operationExcel(object):
    def getSheet(self):
        book = xlrd.open_workbook(filePath("data", "api.xls"))
        return book.sheet_by_index(0)

    @property
    def getRows(self):
        return self.getSheet().nrows

    @property
    def getCols(self):
        return self.getSheet().ncols

    def getValue(self, row, col):
        return self.getSheet().cell_value(row, col)

    def getCaseID(self, row):
        return self.getValue(row=row, col=ExcelValues().getcaseID)

    def getUrl(self, row):
        url = self.getValue(row=row, col=ExcelValues().geturl)
        if "{bookID}" in url:
            url = str(url).replace("{bookID}", readContent())
            return url
        else:
            return url

    def getMethod(self, row):
        return self.getValue(row=row, col=ExcelValues().getmethod)

    def getData(self, row):
        return self.getValue(row=row, col=ExcelValues().getdata)

    def getJson(self, row):
        return self.dictYaml()[self.getData(row=row)]

    def getExpect(self, row):
        return self.getValue(row=row, col=ExcelValues().getexpect)



if __name__ == '__main__':
    # obj = operationExcel()
    # print(obj.getValue(2, 1))
    obj = operationExcel()
    # print(obj.getCaseID(row=4))
    # print(obj.getUrl(row=4))
    # print(obj.getExpect(row=4))
    # print(obj.getMethod(row=4))

    # print(obj.getJson(2))
    # print(type(obj.getJson(2)))


