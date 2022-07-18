#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   parse_qqwry.dat.py.py  
@Datetime:   2022/7/18 10:31
@Contact :   lihanwei@zhiqiansec.com
@Descriptions 
    -

'''
# pip install IPy
from IPy import IP
import os


def query_ip_region(sip) -> tuple:
    """方法用于加载qqwry.dat文件，解析ip归属地
    依赖：`pip install qqwry-py3`, https://github.com/animalize/qqwry-python3
    :param sip:

    :return: tuple/false
    """
    from libs.qqwry import QQwry
    work_dir = os.path.dirname(os.path.abspath(__file__))
    QQWRY_PATH = os.path.join(work_dir, 'libs', "qqwry_lastest.dat")

    # TODO(2022年7月18日): 校验IP
    if None is sip:
        return False
    sip = str(sip)

    q = QQwry()
    ret = q.load_file(QQWRY_PATH)
    if not ret:
        raise FileNotFoundError("%s not found" % QQWRY_PATH)
    q.lookup(sip)
    result = q.lookup(sip)
    return result

if __name__ == '__main__':
    ip = "202.115.32.5"  # ('北京市', '联通')
    r = query_ip_region(ip)
    print(r)

