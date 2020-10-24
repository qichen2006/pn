# -*- coding: utf-8 -*-
# @Time : 2020/10/24 12:26
import allure

from base.method import Requests
from utils.operationExcel2 import operationExcel, ExcelValues

import pytest
import json
from common.public import *

excel = operationExcel()
obj = Requests()


@pytest.mark.parametrize("datas", excel.runs())
def test_login_book(datas):
    # print(datas)
    url = datas[ExcelValues.caseUrl]
    params = datas[ExcelValues.params]

    if len(str(params).strip()) == 0:
        pass
    else:
        params = json.loads(params)

    headers = datas[ExcelValues.headers]

    if len(str(headers).strip()) == 0:
        pass
    else:
        headers = json.loads(headers)
        # print(headers)

    r = obj.post(url=excel.case_prev('login')[ExcelValues.caseUrl],
                 json=json.loads(excel.case_prev('login')[ExcelValues.params]))

    prevResult = r.json()["access_token"]
    # print(prevResult)
    headers = excel.prevHeaders(prevResult)
    # print(type(headers), ">>>>>>>>>>>", headers)

    status_code = int(datas[ExcelValues.status_code])

    # print(">>>>>>>>>",status_code)

    def case_assert_result(r):
        assert r.status_code == status_code
        assert datas[ExcelValues.expect] in json.dumps(r.json(), ensure_ascii=False)

    def setUrl():
        url = str(datas[ExcelValues.caseUrl]).replace("{bookID}", readContent())
        return url

    if datas[ExcelValues.method] == "get":
        if "/books" in datas[ExcelValues.caseUrl]:
            r = obj.get(url=datas[ExcelValues.caseUrl], headers=headers)
            case_assert_result(r=r)
        else:
            r = obj.get(url=setUrl(), headers=headers)
            case_assert_result(r=r)


    elif datas[ExcelValues.method] == "post":
        r = obj.post(url=datas[ExcelValues.caseUrl], json=params, headers=headers)
        bookID = r.json()[0]["datas"]["id"]
        writeContent(content=str(bookID))
        case_assert_result(r=r)

    elif datas[ExcelValues.method] == "put":
        r = obj.put(url=setUrl(), json=params, headers=headers)
        case_assert_result(r=r)

    elif datas[ExcelValues.method] == "delete":

        r = obj.delete(url=setUrl(), headers=headers)
        print(r.json())
        # case_assert_result(r=r)


if __name__ == '__main__':
    # pytest.main(["-sv", "test_login_token_book.py"])

    pytest.main(["-sv", "test_login_token_book.py", "--alluredir", "./report/result"])
    import subprocess


    subprocess.call('allure generate ./report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html', shell=True)


