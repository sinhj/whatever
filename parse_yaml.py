# -*- encoding: utf8 -*-
import os, sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from yaml import safe_load, dump
# python -m pip install pyyaml

conf = safe_load(open("ftp_cfg.yml", 'r'))

print conf["subj"]

print conf["languages"][0]

print conf["ftp_0"]['passwd']
print conf["ftp_1"]['port']

print dump(conf)
