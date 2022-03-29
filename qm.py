# qm.py
#
import logging
import traceback
import requests




def _get(url):
    resp = None

    TIMEOUT = 8
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    try:
        resp = requests.get(url=url, headers=HEADERS, timeout=TIMEOUT, verify=False)

    except Exception as e:
        traceback.print_exc(e)

    finally:
        return resp

class IP_asset:
    """ip实体类，包含归属地等属性
    - ip = '114.67.64.1'
    - netName: JDCOM
    - country: CN
    - descr: Beijing Jingdong 360 Degree E-commerce Co., Ltd.
    - inetnum: 更大的段？
    - fqdn: ?
    """
    def __init__(self, ip):
        # TOdo format!
        self.ip = ip
        self.tcp_port = {
            "22": {
                "service": "ssh",
                "banner": '''HTTP/1.1 200 OK
                            Cache-Control: no-cache
                            Date: Tue, 15 Feb 2022 05:58:47 GMT
                            Content-Length: 0''',
            },
            "80": {
                # todo
            },
        }
        self.udp_port = {
        }


    def quake(self):
        pass

    def fofa(self):
        pass

    def zoomeye(self):
        pass

    def shodan(self):
        pass

    def bing(self):
        pass

    def hunter(self):
        pass

    def whois(self):
        if '' == ip or None == ip:
            exit("ip_whois: ip null!")
        url = f"https://ipwhois.cnnic.cn/bns/query/Query/ipwhoisQuery.do?txtquery={ip}&queryOption=ipv4"
        r = _get(url)
        ## TODO: 解析并保存到类变量中
        logging.info(f"ip_whois:[{r.status_code}][{self.ip}]")
        return(r.text)




if __name__ == '__main__':
    logging.basicConfig(level='INFO', format='%(asctime)s | %(funcName)s()#%(lineno)d |  %(message)s')
    logger = logging.getLogger('qm')
    ip = IP_asset("114.67.64.1")
    ip.whois()
