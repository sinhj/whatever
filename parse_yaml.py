# -*- encoding: utf8 -*-
import os, sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from yaml import load
# python -m pip install pyyaml

conf = load(open("ftp_cfg.yml", 'rb').read())

print conf.get("ftp_0")['passwd']
print conf.get("ftp_1")
