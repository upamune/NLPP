# -*- coding: utf-8 -*-

import sys
import codecs
import re, pprint
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.corpus.util import LazyCorpusLoader

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

# import nltk; nltk.download(); みたいな感じにして jeita をダウンロードする
# ダウンロードした zip ファイルをそのまま読み込む
jeita = LazyCorpusLoader("jeita", ChasenCorpusReader, r".*chasen", encoding="utf-8")
# print '/'.join( jeita.words()[22100:22140] )

# タグ情報はタブ区切りの文字列になっており、読み、原形、品詞1 、品詞2 、活用形の情報が含まれている
print '\nEOS\n'.join(['\n'.join("%s/%s" % (w[0],w[1].split('\t')[2]) for w in sent) for sent in jeita.tagged_sents()[2170:2173]])
