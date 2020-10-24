# -*- coding: utf-8 -*-
# @Time : 2020/10/19 22:21


from requests import request


class Requests(object):
    def request(self, url, method="get", **kwargs):
        if method == "get":
            return request(method=method, url=url, **kwargs)
        elif method == "post":
            return request(method=method, url=url, **kwargs)
        elif method == "put":
            return request(method=method, url=url, **kwargs)
        elif method == "delete":
            return request(method=method, url=url, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method="post", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url=url, method="put", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url=url, method="delete", **kwargs)
