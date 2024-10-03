import re
class Search:
    def __init__(self,filename) :
        self.filename = filename

    def clean(self,elem) :
        res = re.sub('[^A-Za-z0-9]+', ' ', elem)
        return res

    def getLine(self,word):
        file = open(self.filename,"r")
        lst = [word]
        for index, line in enumerate(file):
            if word in line : 
                lineNumber = index + 1
                line = line.rstrip("\n")
                line = self.clean(line)
                tpl = (lineNumber, line)
                lst.append(tpl)
        return lst
        if len(lst) < 1 :
            print("Word not found")
        else :
            print(lst)
        file.close()

