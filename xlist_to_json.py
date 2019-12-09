import pprint
import read_outfiles

class xinfo_to_clusterjson:

    def __init__(self, xinfodict):
        self.xinfodict = xinfodict
    
    def create_dict_forexcel(self):
        xmsdict = {}
        for clusterinfo in self.xinfodict['clusters']:
            xmsdict[clusterinfo[0]] = []
        return xmsdict
        
if __name__ == '__main__':
    testdict = read_outfiles.concatinate_to_dict('xmcli')
    forexldict = xinfo_to_clusterjson(testdict).create_dict_forexcel()
    print(forexldict)



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