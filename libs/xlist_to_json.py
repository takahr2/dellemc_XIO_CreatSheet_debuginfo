import pprint
import libs.read_outfiles as readfile
import json
import os

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
        
        for snapshotsetinfo in self.xinfodict['snapsets']:
            snapsetsub = {}
            snapsetsub['SnapShotSet-Name'] = snapshotsetinfo[0]
            snapsetsub['Index'] = snapshotsetinfo[1]
            snapsetsub['Consistency-Group-Name'] = snapshotsetinfo[2]
            snapsetsub['cluster-Name'] = snapshotsetinfo[3]
            snapsetsub['Volume-List'] = snapshotsetinfo[4:]

            xmsdict[snapshotsetinfo[3]][0]['snapsets'].append(snapsetsub)
        
        for cginfo in self.xinfodict['cg']:
            cgsub = {}
            cgsub['CG-Name'] = cginfo[0]
            cgsub['index'] = cginfo[1]
            cgsub['Cluster-Name'] = cginfo[2]            
            cgsub['Volume-List'] = cginfo[3:]
            xmsdict[cginfo[2]][0]['cg'].append(cgsub)
        
        for targetinfo in self.xinfodict['targets']:
            targetsub = {}
            targetsub['Target-Name'] = targetinfo[0]
            targetsub['index'] = targetinfo[1]
            targetsub['cluster-Name'] = targetinfo[2]
            targetsub['Port-Type'] = targetinfo[4]
            targetsub['Port-Address'] = targetinfo[5]
            targetsub['Port-State'] = targetinfo[8]
            targetsub['Storage-Controller-Name'] = targetinfo[10]

            xmsdict[targetinfo[2]][0]['targets'].append(targetsub)

        for initiatorinfo in self.xinfodict['initiators']:
            initiatorsub = {}
            initiatorsub['Initiator-Name'] = initiatorinfo[0]
            initiatorsub['Index'] = initiatorinfo[1]
            initiatorsub['Cluster-Name'] = initiatorinfo[2]
            initiatorsub['Port-Type'] = initiatorinfo[4]
            initiatorsub['Port-Address'] = initiatorinfo[5]
            initiatorsub['IG-Name'] = initiatorinfo[6]
            initiatorsub['Initiator-OS'] = initiatorinfo[-1].rstrip()

            xmsdict[initiatorinfo[2]][0]['initiators'].append(initiatorsub)

        xmsjson = json.dumps(xmsdict)

        return xmsjson, xmsdict

def json_dump(jsonfile, filename):
    parsed = json.loads(jsonfile)
    outputpath = os.path.join('output', filename)
    with open(outputpath, 'w') as xjson:
        json.dump(parsed, xjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(', ', ': '))
    return xjson


if __name__ == '__main__':
    ### unittest
    testdict = readfile.concatinate_to_dict('C:\\Users\\takahr2\\Projects\\git\\dellemc_XIO_CreatSheet_debuginfo\\input\\small\\xms\\xmcli')
    #pprint.pprint(testdict['initiators'])
    xmsjson, forexldict = xinfo_to_clusterjson(testdict).create_dict_forexcel()
    #pprint.pprint(forexldict['XtremIO_01_L'][0]['initiators'])
    json_dump(xmsjson, 'xio.json')

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