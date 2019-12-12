import pprint
import libs.debuginfo_extract as extract
import libs.read_outfiles as outfiles
import libs.xlist_to_json as xjson
import os
import pathlib

def debuginfo_to_json():
    inputdirlist= pathlib.Path('input').iterdir()
    fileidx = 1
    for difile in inputdirlist:
        if '.tar' in difile.name:
            xmclidir = extract.debuginfo_extract(difile).xmcli_extract()
            print(xmclidir)

            xiorawdict = outfiles.concatinate_to_dict(xmclidir)
            #print(xiodict)

            xiojson, xiosepdict = xjson.xinfo_to_clusterjson(xiorawdict).create_dict_forexcel()
            #print(xiojson)
            jsonfilename = str(fileidx) + '_xio.json'
            jsonfile = xjson.json_dump(xiojson, jsonfilename)
            fileidx += 1


if __name__ == '__main__':
    debuginfo_to_json()
    

