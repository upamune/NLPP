# -*- coding: utf-8 -*-

import sys
import codecs
import re, pprint
import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

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


jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')

ginga = PlaintextCorpusReader("../data/", r"gingatetsudono_yoru.txt",
                              encoding="utf-8",
                              para_block_reader=read_line_block,
                              sent_tokenizer=jp_sent_tokenizer,
                              word_tokenizer=jp_chartype_tokenizer)

# 平文を表示
# print ginga.raw()

# トークンを列挙
print '/'.join(ginga.words())

# Text オブジェクトに変換した後コンコーダンスを表示
# コンコーダンスは、指定された単語が現れた場所を、その周辺の文章とともに表示する。
ginga_t = Text( w.encode('utf-8') for w in ginga.words() )
ginga_t.concordance("川")

