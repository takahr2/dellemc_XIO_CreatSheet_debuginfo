import pprint
import libs.debuginfo_extract as extract
import libs.read_outfiles as outfiles
import libs.xlist_to_json as xjson
import libs.xjson_to_dws as todws
import os
import pathlib

def debuginfo_to_json():
    inputdirlist = pathlib.Path('input').iterdir()
    fileidx = 1
    xjsonlist = []
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
            xjsonpath = os.path.join('output', jsonfilename)
            print(xjsonpath)
            xjsonfullpath = os.path.abspath(xjsonpath)

            xjsonlist.append(xjsonfullpath)
        
    return xjsonlist

def createxdws(jsonlist):
    output = os.path.abspath('output')
    template =  os.path.abspath('template\\3_XtremIO_Template_Design_Worksheet_v1.0.xlsx')
    
    for xjson in jsonlist:
        todws.create_xdws(xjson).createdws(template, output)
    
        
def main():
    xjsonfilelist = debuginfo_to_json()
    createxdws(xjsonfilelist)
    print('XtremIO Design Worksheet Creation is Finish')
    while True:
        finishinput = input('Please input Enter kye to finish...')
        if not finishinput:
            break


if __name__ == '__main__':
    main()
    

