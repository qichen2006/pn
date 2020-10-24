# -*- coding: utf-8 -*-
# @Time : 2020/10/19 22:58


import yaml

from common.public import filePath


class OperationYaml(object):
    def readYaml(self, fileDir="", fileName=""):
        with open(filePath(fileDir, fileName), "r", encoding="utf-8") as f:
            # print(yaml.safe_dump_all(f))
            return list(yaml.safe_load_all(f))

    def dictYaml(self, fileDir="config", fileName="books.yaml"):
        total = {}
        with open(filePath(fileDir, fileName), "r", encoding="utf-8") as f:
            r = list(yaml.safe_load_all(f))
            # print(r)
            for item in r:
                k = list(item.keys())[0]
                v = list(item.values())[0]
                total[k] = v

        # print(total)
        return total


if __name__ == '__main__':
    obj = OperationYaml()

    # r = obj.readYaml("data", "login.yaml")
    # for item in r:
    #     print(item)

    r = obj.dictYaml()
    print(r)
