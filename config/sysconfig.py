# -*-coding:utf-8 -*-
# author: zeyang@staff.sina.com.cn
# time:   2013-12-12

import os
_WORKSPACE = os.getcwd()[:-7]

# test app information.
_SOURCE = "4125898983"
_ACCESS_TOKEN = "2.00mG98WBnnqNVEfe7acc1871Kgp6XC"

# api reference information
apiRef = {
'status':\
	{'apis':['queryid','querymid','show'],\
	'name':'微博组接口',\
	'path':_WORKSPACE + '/data/api/status'},
'open':\
	{'apis':[],
	'name':'平台组接口',
	'path':_WORKSPACE + '/data/api/open'},
'oauth':\
	{'apis':[],\
	'name':'授权组接口',\
	'path':_WORKSPACE + '/data/api/oauth'}
}

# work dict path
_PLANPATH = _WORKSPACE + '/plan'
_APIPATH = _WORKSPACE + '/data/api'
_CASEPATH = _WORKSPACE + '/data/case'
