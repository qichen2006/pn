# -*- coding: utf-8 -*-
# @Time : 2020/10/21 23:02

from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcel import operationExcel
import pytest
import json
from common.public import *


class TestBook(object):
    excel = operationExcel()
    obj = Requests()

    def result(self, r, row):
        assert r.status_code == 200
        assert self.excel.getExpect(row=row) in json.dumps(r.json(), ensure_ascii=False)

    def test_book_001(self):
        """获取所有书籍信息"""
        r = self.obj.get(url=self.excel.getUrl(row=1))
        print(r.json())
        print(">>>>>>>>", self.excel.getExpect(row=1))
        # assert self.excel.getExpect(row=1) in json.dumps(r.json(),ensure_ascii=False)
        self.result(r=r, row=1)

    def test_book_002(self):
        """添加书籍"""
        r = self.obj.post(url=self.excel.getUrl(row=2), json=self.excel.getJson(row=2))
        bookID = r.json()[0]["datas"]["id"]
        writeContent(content=bookID)
        self.result(r, row=2)

    def test_book_003(self):
        """查看书籍"""
        r = self.obj.get(url=self.excel.getUrl(row=3))
        # print(r.json()
        self.result(r=r, row=3)

    def test_book_004(self):
        """编辑书籍信息"""
        r = self.obj.put(url=self.excel.getUrl(row=4),
                         json=self.excel.getJson(row=4))
        self.result(r=r, row=4)

    def test_book_005(self):
        """删除书籍信息"""
        r = self.obj.delete(url=self.excel.getUrl(row=5))
        self.result(r=r, row=5)


if __name__ == '__main__':
    # pytest.main(["-sv", "test_book.py::TestBook::test_book_003"])
    pytest.main(["-sv", "test_book.py::TestBook"])
