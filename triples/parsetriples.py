import re
import triples.triple as Triple

class ParseTriples():

    def __init__(self,filename):
        super().__init__
        self._filename = filename
        self._file = open(filename, "r", errors='ignore')

    def getNext(self):
        if(self._file.closed):
            return None
        
        line = self._file.readline()
        while((isinstance(line,str)) and line.startswith("#")):
            line = self._file.readline()

        if(not line):
            return None

        m = re.match('<(.+)>\s*<(.+)>\s*[<"](.+)[>"]',line.strip())
        if(m):
            ret = Triple.Triple(m.group(1),m.group(2),m.group(3))
            return ret
            
        else:
            return

