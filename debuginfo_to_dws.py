import pprint
import libs.debuginfo_extract as extract
import libs.read_outfiles as outfiles
import libs.xlist_to_json as xjson
import os
import pathlib

def debuginfo_to_json():
    inputdirlist= pathlib.Path('input').iterdir()
    for difile in inputdirlist:
        if '.tar' in difile.name:
            extract.debuginfo_extract(difile).xmcli_extract()

if __name__ == '__main__':
    debuginfo_to_json()
    

