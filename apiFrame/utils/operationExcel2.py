# -*- coding: utf-8 -*-
# @Time : 2020/10/20 22:06

import xlrd
from common.public import filePath, readContent
import json


class ExcelValues(object):
    caseID = "测试用例ID"
    caseModel = "模块"
    caseName = "接口名称"
    caseUrl = "请求地址"
    casePre = "前置条件"
    method = "请求方法"
    paramsType = "请求参数类型"
    params = "请求参数"
    expect = "期望结果"
    isRun = "是否运行"
    headers = "请求头"
    status_code = "状态码"


class operationExcel(object):
    def getSheet(self):
        book = xlrd.open_workbook(filePath("data", "api.xls"))
        return book.sheet_by_index(0)

    @property
    def getExcelDatas(self):
        title = self.getSheet().row_values(0)
        datas = []
        for row in range(1, self.getSheet().nrows):
            row_values = self.getSheet().row_values(row)
            datas.append(dict(zip(title, row_values)))
        return datas

    def runs(self):
        run_list = []
        for item in self.getExcelDatas:
            isRun = item[ExcelValues.isRun]
            if isRun == "y":
                run_list.append(item)
            else:
                pass
            # print(isRun)
        return run_list

    def case_list(self):
        cases = []
        for item in self.getExcelDatas:
            cases.append(item)
        return cases

    def params(self):
        for item in self.runs():
            params = item[ExcelValues.params]
            # print(params)
            if len(str(params).strip()) == 0:
                pass
            else:
                # print(params)
                # print(type(params))
                r = json.loads(params)
                # print(r, ">>>>>>>>>>", type(r))
                yield r

    def case_prev(self, casePrev):
        for item in self.case_list():

            if item[ExcelValues.caseID] == casePrev:

                # print(">>>>>>>>>>>", item)
                return item
            else:
                return None

    def prevHeaders(self, prevResult):
        for item in self.runs():
            headers = item[ExcelValues.headers]
            # print(headers)
            if "{token}" in headers:
                headers = str(headers).replace("{token}", prevResult)
                return json.loads(headers)


if __name__ == '__main__':
    obj = operationExcel()

    # r = obj.getExcelDatas
    # # print(r)
    # for item in r:
    #     print(item[ExcelValues.caseUrl])

    # for item in obj.runs():
    #     print(item)

    # r = obj.params()
    # for x in r:
    #     print(x, ">>>>>>>>>>>>>", type(x))
    # r = obj.case_prev("login")[ExcelValues.caseUrl]
    # print(r)
    # obj.prevHeaders("")
    r=obj.case_list()
    print(r)