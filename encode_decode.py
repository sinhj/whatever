# -*- encoding: utf-8 -*-



# str 的本质是编码，打印到屏幕之前要解码为 Unicode 码点
# type 'unicode' 即 Unicode 码点 一一映射 字符，是确定字符意义的标识

a = "一去二三里, 离地四五丈"      # type 'str'
# print a 在 cmd prompt 执行，默讱是 GBK
# print a.decode("gbk", "ignore")

b = u"一去二三里, 离地四五丈"     # type 'unicode'
c = a.decode("utf-8")           # type 'unicode'
print b == c
print c + '\n'



# 编码 encode 字符 -> 代码
# 解码 decode 代码 -> 字符
# 'str' decode => 'unicode'
# 'unicode' encode => 'str'



s = "我可去"
s_dec = s.decode("utf-8")               # type 'unicode'

s_utf8 = s_dec.encode("utf-8")              # type str
print s_utf8 == "我可去"

s_unic = s_dec.encode("unicode_escape")     # type str
print s_unic == "\u6211\u53ef\u53bb"

print s_unic.decode("unicode_escape")

print s_dec.encode("gbk").decode("gbk")



# 文本的内容是编出的码，读取出来是 type 'str', 以不同的解码方式，解码成不同的 Unicode 码点
# type 'unicode' 不能写入到文件

# 读取 GBK 编码的文本
print "\nGBK"
for elem in open(r".\gbk.txt"):
    print elem              # cmd prompt 默讱 GBK 解码，不会乱码
    print elem.decode("gbk")

# 读取 GB18030 编码的文本
print "\nGB18030"
for elem in open(r".\gb18030.txt"):
    print elem              # GB18030 兼容 GBK, 不会乱码
    print elem.decode("gb18030")

# 读取 UTF-8 编码的文本
print "\nUTF-8"
for elem in open(r".\utf-8.txt"):
    print elem              # cmd prompt 默讱 GBK 解码，会乱码
    print elem.decode("utf-8")

# 读取 UTF-16 LE without BOM 编码的文本
print "\nUTF-16 LE"
for elem in open(r".\utf-16le.txt"):
    print elem.decode("utf-16le")
