<<<<<<< HEAD
# QueryMe
全面的资产信息查询工具（IP、域名）
=======
# 介绍
QueryMe，是一款资产信息查询工具，也类似于资产情报查询平台，只不过情报要做到最全！。

渗透中，常常需要查询单个资产（IP、域名）的信息，包括isp运营商，IP归属地、开放端口服务、历史SSL证书、历史解析过的域名等信息，但渗透的时候一个个商平台查，真的好傻啊。

## ToDo：
- 通过 `qm 127.0.0.1` 来调用
- 考虑整合各种osint平台
    - fofa……
    - oneforall接口
    - poc-t的接口
    - arl的接口
    - riskiq, sucurityTrail

## 后期
- 考虑做缓存，避免浪费太多api次数
- c段的quicklook，再议。
- 主动模式、被动模式（有点像amass。再议）
>>>>>>> 7fc2587 (feat(Add): +cnnic ipwhois)
