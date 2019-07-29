# -*- encoding: utf8 -*-
import os, sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from yaml import safe_load
# python -m pip install pyyaml

conf = safe_load(open("ftp_cfg.yml", 'r'))

print conf.get("subj")

print conf.get("languages")[0]

print conf.get("ftp_0")['passwd']
print conf.get("ftp_1")['port']
