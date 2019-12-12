import tarfile
import os

class debuginfo_extract:

    def __init__(self, xtgzfile):
        self.xtgzfile = xtgzfile
    
    def xmcli_extract(self):

        with tarfile.open(self.xtgzfile, 'r:*') as xtarfile:

            xmclidir = []
            for dirname in xtarfile.getmembers():
                if 'xmcli' in dirname.name:
                    xmclidir.append(dirname)
            #print(xmclidir)
            workfolder = 'work'        
            xtarfile.extractall(workfolder, members=xmclidir)
            xmclitopdir = os.path.join(workfolder, xmclidir[0].name.replace('events_history.csv', ''))

        return xmclitopdir

def test():
    filename = input('ファイル名を入力 :')
    dirnames = debuginfo_extract(filename).xmcli_extract()
    print(dirnames)

if __name__ == '__main__':
    test()


