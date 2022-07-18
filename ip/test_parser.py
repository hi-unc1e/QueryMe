#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   test_parser.py
@Datetime:   2022/7/18 10:41
@Contact :   lihanwei@zhiqiansec.com
@Descriptions
    -
'''
from unittest import TestCase
from ip.parser import query_ip_region


class Test(TestCase):
    def test_query_ip_should_be(self):
        SHOULD_BE = {
            '127.0.0.1':     ('本机地址', ' CZ88.NET'),
            '0.0.0.0':       ('IANA', '保留地址'),
            ' 8.8.8.8 ':     ('美国', '加利福尼亚州圣克拉拉县山景市谷歌公司DNS服务器'),

        }
        for k,v in SHOULD_BE.items():
            self.assertEqual(query_ip_region(k), v)

    def test_query_ip_should_NOT_be(self):
        with self.assertRaises(OSError):
            query_ip_region('1.2.3.')
        self.assertFalse(query_ip_region(None))
