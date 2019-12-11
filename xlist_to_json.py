import pprint
import read_outfiles
import json

class xinfo_to_clusterjson:

    def __init__(self, xinfodict):
        self.xinfodict = xinfodict
    
    def create_dict_forexcel(self):
        
        xmsdict = {}       
        
        for xmsinfo in self.xinfodict['xms']:
            xmsdict[xmsinfo[0] ]= {
                'name': xmsinfo[0],
                'SW-Version': xmsinfo[2],
                'Xms-IP-Addr-With-Subnet': xmsinfo[3]}

        for clusterinfo in self.xinfodict['clusters']:
            xmsdict[clusterinfo[0]] = [{
                'clusterinfo': [],
                'volumeinfo': [],
                'lunmappings': [],
                'snapsets': [],
                'cg': [],
                'targets': [],
                'initiators': []
                }]
        
        for clusterinfo in self.xinfodict['clusters']:
            clusterinfosub = {}
            clusterinfosub['cluster-Name'] = clusterinfo[0]
            clusterinfosub['index'] = clusterinfo[1]
            clusterinfosub['SW-Version'] = clusterinfo[14]
            clusterinfosub['SerialNumber'] = clusterinfo[15]

            xmsdict[clusterinfo[0]][0]['clusterinfo'].append(clusterinfosub)
        
        for volumeinfo in self.xinfodict['volumes']:
            volumeinfosub = {}
            volumeinfosub['Volume-Name'] = volumeinfo[0]
            volumeinfosub['index'] = volumeinfo[1]
            volumeinfosub['cluster-Name'] = volumeinfo[2]
            volumeinfosub['Vol-Size'] = volumeinfo[4]
            volumeinfosub['NAA-Identifier'] = volumeinfo[14]

            xmsdict[volumeinfo[2]][0]['volumeinfo'].append(volumeinfosub)

        for lunmappingsinfo in self.xinfodict['lunmappings']:
            mappingssub = {}
            mappingssub['Cluster-Name'] = lunmappingsinfo[0]
            mappingssub['index'] = lunmappingsinfo[3]
            mappingssub['Volume-Name'] = lunmappingsinfo[2]
            mappingssub['IG-Name'] = lunmappingsinfo[4]
            mappingssub['HLU'] = lunmappingsinfo[8]

            xmsdict[lunmappingsinfo[0]][0]['lunmappings'].append(mappingssub)

        xmsjson = json.dumps(xmsdict)

        return xmsjson, xmsdict

def json_dump(jsonfile):
    parsed = json.loads(jsonfile)
    with open('xio.json', 'w') as xjson:
        json.dump(parsed, xjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(', ', ': '))


if __name__ == '__main__':
    testdict = read_outfiles.concatinate_to_dict('latest/xms/xmcli')
    print(testdict['snapsets'])
    xmsjson, forexldict = xinfo_to_clusterjson(testdict).create_dict_forexcel()
    #pprint.pprint(forexldict['XtremIO_01_L'][0]['lunmappings'])
    json_dump(xmsjson)

    #pprint.pprint(forexldict['xms'])
    #pprint.pprint(forexldict)



'''
    xiodict = {
        'xms': xms,
        'clusters': clusters,
        'volumes': volumes,
        'lunmappings': lunmappings,
        'snapsets': snapsets,
        'cg': cg,
        'targets': targets,
        'initiators': initiators
        }
'''