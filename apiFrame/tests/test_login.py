# -*- coding: utf-8 -*-
# @Time : 2020/10/19 23:12


import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
import json

obj = Requests()
objYaml = OperationYaml()


@pytest.mark.parametrize("datas", objYaml.readYaml("data", "login.yaml"))
def test_login(datas):
    r = obj.post(url=datas['url'], json=datas['data'])
    # print(r.text)
    # print(json.dumps(r.json(),ensure_ascii=False))
    assert datas['expect'] in json.dumps(r.json(), ensure_ascii=False)


if __name__ == '__main__':
    pytest.main(["-sv", "test_login.py"])
