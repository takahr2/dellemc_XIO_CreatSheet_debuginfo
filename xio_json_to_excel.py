import json
import pandas as pd
import pprint

class xio_json_to_excel:

    def __init__(self, jsonfile):
        self.jsonfile = jsonfile

    def json_read_forDWS_df(self):
        with open(self.jsonfile) as f:
            jsondict = json.load(f)
            voldict = {}
            voldict["vol"] = jsondict["Volume"]
            jsondf = pd.DataFrame(voldict)
        
        return jsondf

    def json_read_dict(self):
        with open(self.jsonfile) as f:
            
            jsondict = json.load(f)
        
        return jsondict

    

def main():
    xjsonfile = input('jsonファイルを入力して下さい ：')
    xjson = xio_json_to_excel(xjsonfile)
    jsondf = xjson.json_read_forDWS_df()

    pprint.pprint(jsondf)

if __name__ == '__main__':
    main()

