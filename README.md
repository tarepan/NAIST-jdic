<div align="center">

# 📖 NAIST Japanese Dictionary 📖 <!-- omit in toc -->

NAIST Japanese Dictionary, Japanese word/morpheme dictionary containing around 500,000 entries.  
NAIST Japanese Dictionary は 50 万エントリーに迫る単語/形態素を含んだ、形態素解析向け日本語辞書です。  

</div>

## About this repository
This repository is unofficial clone of *NAIST-jdic* (NAIST Japanese Dictionary, `naist-jdic` & `mecab-naist-jdic`).  
*NAIST-jdic* has many versions, so this repository controls these versions with `git`.  
You can easily browse dictionary entries, check diffs, clone for your project 😉  

## Contents list
*NAIST-jdic* for MeCab, `mecab-naist-jdic`, is under [`mecab-naist-jdic-RAW` branch](https://github.com/tarepan/NAIST-jdic/tree/mecab-naist-jdic-RAW) without any modification.  
For convenience, UTF8-nized `mecab-naist-jdic` is also prepared and is under [`mecab-naist-jdic-UTF8` branch](https://github.com/tarepan/NAIST-jdic/tree/mecab-naist-jdic-UTF8).  

*NAIST-jdic* for ChaSen, `naist-jdic` is under [`naist-jdic-RAW` branch](https://github.com/tarepan/NAIST-jdic/tree/naist-jdic-RAW) without any modification.  
For convenience, UTF8-nized `naist-jdic` is also prepared and is under [`naist-jdic-UTF8` branch](https://github.com/tarepan/NAIST-jdic/tree/naist-jdic-UTF8).  

Full list of versions is below (all versions have `RAW` and `UTF8`).  

| `mecab-naist-jdic` | `naist-jdic` | Windows Binary Edition |
| :----------------: | :----------: | :--------------------: |
|  v0.6.3b-20111013  |              |                        |
|  v0.6.3-20100801   |              |                        |
|  v0.6.2-20100208   |              |                        |
|  v0.6.1-20090630   |              |                        |
|  v0.6.0-20090616   |              |                        |
|  v0.5.0-20090512   |              |                        |
|  v0.4.3-20080917   |              |                        |
|  v0.4.3-20080812   |              |                        |
|  v0.4.3-20080723   |    v0.4.3    |                        |
|                    |    v0.4.2    |                        |
|                    |    v0.4.1    |                        |
|                    |    v0.4.0    |                        |
|  v0.3.0-20080309   |    v0.3.0    |                        |
|  v0.2.0-20080229   |    v0.2.0    |                        |
|                    |              |         v0.1.0         |

All `RAW` versions have version tags.  

Prerelease versions and ChaSen exe files exist in [Origin](#Origin), but I decided to remove them from git. If you need, check Origin.  

## Origin
[Origin *NAIST-jdic* project page](https://ja.osdn.net/projects/naist-jdic/) seems to be lost (`503 Service Temporarily Unavailable` at 2025-06-09).  
All source codes are cloned from [http://iij.dl.sourceforge.jp](http://iij.dl.sourceforge.jp/naist-jdic/).  
I'd like to express my gratitude to everyone concerned.  

## How to Make
1. Download all version from [http://iij.dl.sourceforge.jp](http://iij.dl.sourceforge.jp/naist-jdic/)
2. Expand these `.tar.gz`
3. Commit raws with tag
4. Make UTF-8 variants with `./eucjp_to_utf8.py` and manual PDF move
5. Commit them
