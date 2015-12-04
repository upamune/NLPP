# -*- coding: utf-8 -*-

import sys
import codecs
import re, pprint

# 日本語を含む文字列を標準入出力とやり取りするのに必要
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

# sys.setdefaultencodingを使えるようにリロードする
reload(sys)
# デフォルトのエンコーディングをUTF-8にセット
sys.setdefaultencoding('utf-8')


# Unicode文字をエスケープせずに出力する
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)

data = {
    u"スクリプト言語":
        {u"Perl": u"パール",
         u"Python": u"パイソン",
         u"Ruby": u"ルビー"},
    u"関数型言語":
        {u"Erlang": u"アーラング",
         u"Haskell": u"ハスケル",
         u"Lisp": u"リスプ"}
}

print "%s で %s" % (u"パイソン", u"自然言語処理")

print data
print pp(data)
