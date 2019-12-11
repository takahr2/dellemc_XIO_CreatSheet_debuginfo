import pathlib
import pprint

class read_xmclioutfiles:

    def __init__(self, xmclifolder):
        self.xmclifolder = xmclifolder
    
    def read_showclustersinfoout(self):
        showclusteroutpath = pathlib.Path(self.xmclifolder + '\\ShowClustersInfo.out')
        with open (showclusteroutpath, mode='r', encoding='utf-8') as showclusterout:
            clusters = []
            for index, clusterinfo in enumerate(showclusterout):
                if index == 0:
                    pass
                else:
                    cluster = clusterinfo.split(' ')
                    cluster = [a for a in cluster if a != '']
                    clusters.append(cluster)
            
        return clusters

    def read_showxmsout(self):
        showxmsoutpath = pathlib.Path(self.xmclifolder + '\\ShowXms.out')
        with open (showxmsoutpath, mode='r', encoding='utf-8') as showxmsout:
            xmslist = []
            for index, xmsinfo in enumerate(showxmsout):
                if index == 0:
                    pass
                else:
                    xms = xmsinfo.split(' ')
                    xms = [a for a in xms if a != '']
                    xmslist.append(xms)
            
        return xmslist

    def read_showtargetsout(self):
        showtargetsoutpath = pathlib.Path(self.xmclifolder + '\\ShowTargets.out')
        with open (showtargetsoutpath, mode='r', encoding='utf-8') as showtargetsout:
            targets = []
            for index, targetinfo in enumerate(showtargetsout):
                if index == 0:
                    pass
                else:
                    target = targetinfo.split(' ')
                    target = [a for a in target if a != '']
                    targets.append(target)
            
        return targets

    def read_showinitiatorsout(self):
        showinitiatorsoutpath = pathlib.Path(self.xmclifolder + '\\ShowInitiators.out')
        with open (showinitiatorsoutpath, mode='r', encoding='utf-8') as showinitiatorsout:
            initiators = []
            for index, initiatorinfo in enumerate(showinitiatorsout):
                if index == 0:
                    pass
                else:
                    initiator = initiatorinfo.split(' ')
                    initiator = [a for a in initiator if a != '']
                    initiators.append(initiator)
            
        return initiators

    def read_showvolumesout(self):
        showvolumeoutpath = pathlib.Path(self.xmclifolder + '\\ShowVolumes.out')
        with open(showvolumeoutpath, mode='r', encoding='utf-8') as showvolumeout:
            volumes = []
            for index, volumeinfo in enumerate(showvolumeout):
                if index == 0:
                    pass
                else:
                    volume = volumeinfo.split(' ')
                    volume = [a for a in volume if a != '']
                    volumes.append(volume)
            
        return volumes
    
    def read_showlunmappingsout(self):
        showlonmappingsoutpath = pathlib.Path(self.xmclifolder + '\\ShowLunMappings.out')
        with open(showlonmappingsoutpath, mode = 'r', encoding='utf-8') as showlonmappingsout:
            lunmappings = []
            for index, lunmappinginfo in enumerate(showlonmappingsout):
                if index == 0:
                    pass
                else:
                    lunmapping = lunmappinginfo.split(' ')
                    lunmapping = [a for a in lunmapping if a != '']
                    lunmappings.append(lunmapping)
        
        return lunmappings
    
    def read_showallsnapshotsetout(self):
        showallsnapshotsetpath = pathlib.Path(self.xmclifolder + '\\ShowAllSnapshotsSet.out')
        with open(showallsnapshotsetpath, mode='r', encoding='utf-8') as showallsnapshotsetout:
            snapshotsets = []
            snapsetsublist = []
            memberflag = 0
            for index, snapshotsetinfo in enumerate(showallsnapshotsetout):                
                snapshotsetinforow = snapshotsetinfo.split(':')

                if memberflag == 0 and snapshotsetinforow[0] != '		Name' and  snapshotsetinforow[0] == 'Name':                
                    snapshotsets.append(snapsetsublist)
                    snapsetsublist = []
                    memberflag = 1
                    snapsetname = ''.join(snapshotsetinforow[1].rstrip().lstrip())
                    snapsetsublist.append(snapsetname)
            
                elif snapshotsetinforow[0] == 'Consistency-Group-Name':
                    cgname = ''.join(snapshotsetinforow[1].rstrip().lstrip())
                    snapsetsublist.append(cgname)
                
                elif snapshotsetinforow[0] == 'Cluster-Id':
                    cluster = snapshotsetinforow[1].split('\'')
                    cluster = cluster[3]
                    snapsetsublist.append(cluster)
                
                elif snapshotsetinforow[0] == 'Volume-List':
                    memberflag = 0
                
                elif snapshotsetinforow[0] == '		Name':
                    snaps = ''.join(snapshotsetinforow[1].rstrip().lstrip())
                    snapsetsublist.append(snaps)
            
            snapshotsets.append(snapsetsublist)
            snapshotsets = snapshotsets[1:]
            
        return snapshotsets

    def read_allshowcgout(self):
        showcgoutpath = pathlib.Path(self.xmclifolder + '\\ShowAllConsistencyGroups.out')
        with open(showcgoutpath, mode='r', encoding='utf-8') as showcgout:
            ConsistencyGroups = []
            cgsublist = []
            memberflag = 0
            for index, cginfo in enumerate(showcgout):                
                cgrow = cginfo.split(':')

                if memberflag == 0 and cgrow[0] != '		Name' and  cgrow[0] == 'Name':                
                    ConsistencyGroups.append(cgsublist)
                    cgsublist = []
                    memberflag = 1
                    cgname = ''.join(cgrow[1].rstrip().lstrip())
                    cgsublist.append(cgname)
            
                elif cgrow[0] == 'Cluster-Id':
                    cluster = cgrow[1].split('\'')
                    cluster = cluster[3]
                    cgsublist.append(cluster)
                
                elif cgrow[0] == 'Volume-List':
                    memberflag = 0
                
                elif memberflag == 0 and cgrow[0] == '		Name':
                    snaps = ''.join(cgrow[1].rstrip().lstrip())
                    cgsublist.append(snaps)
            
            ConsistencyGroups.append(cgsublist)
            ConsistencyGroups = ConsistencyGroups[1:]
            
        return ConsistencyGroups

def concatinate_to_dict(xmcli):
    xmcli = xmcli
    readxmcli = read_xmclioutfiles(xmcli)
    clusters = readxmcli.read_showclustersinfoout()
    volumes = readxmcli.read_showvolumesout()
    lunmappings = readxmcli.read_showlunmappingsout()
    snapsets = readxmcli.read_showallsnapshotsetout()
    cg = readxmcli.read_allshowcgout()
    xms = readxmcli.read_showxmsout()
    targets = readxmcli.read_showtargetsout()
    initiators = readxmcli.read_showinitiatorsout()
    #print(clusters)
    #print(volumes)
    #print(lunmappings)
    #print(snapsets)
    #print(cg)
    #print(xms)
    #print(targets)
    #print(initiators)
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
    return xiodict

if __name__ == '__main__':
    xmclidir = 'latest/xms/xmcli'
    xio = concatinate_to_dict(xmclidir)
    print(xio['cg'])

