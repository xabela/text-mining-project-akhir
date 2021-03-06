import math
import numpy as np
from statistics import mean

class Weight:
    def __init__(self):
        self.file2 = []
        self.temp = []
        self.TF = []
        self.IDF = []
        self.TFIDF = []
        self.normal = []

    def setText(self, inp):
        self.file2 = inp

    def getFeatures(self):
        for x in self.file2:
            for words in x:
                if words not in self.temp:
                    self.temp.append(words)

        return self.temp

    def getTF(self):
        for feature in self.temp:
            document_count = []
            for document in self.file2:
                if document.count(feature) == 0:
                    document_count.append(document.count(feature))
                else:
                    ct = 1 + math.log10(document.count(feature))
                    document_count.append(ct)

            self.TF.append(document_count)

        return self.TF

    def getIDF(self):
        q = 0
        DF = []
        leng = len(self.file2)

        for x in self.TF:
            for y in x:
                if y != 0:
                    q += 1
            DF.append(q)
            q = 0

        for z in DF:
            s = math.log10(leng / z)
            self.IDF.append(s)

        return self.IDF
        
    def getTFIDF(self):
        temp = []
        count = 0

        for i in self.IDF:
            for j in range(count, len(self.TF)):
                for k in self.TF[j]:
                    res = i * k

                    temp.append(res)
                self.TFIDF.append(temp)
                temp = []
                count += 1
                break

        return self.TFIDF

    def getNormal(self):
        normalTemp = []
        temp = []
        sm = 0
        tpose = tuple(zip(*self.TFIDF))
		
        # for row in tpose:
        for x in range(len(tpose)):
            for i in tpose[x]:
                sm += math.pow(i, 2)
                sms = math.sqrt(sm)
            normalTemp.append(sms)
            sm = 0
            
        for row in self.TFIDF:
            for i in range(len(row)):
                if (normalTemp[i] != 0):
                    total = row[i] / normalTemp[i]
                else:
                    total = 0
                temp.append(total)
            self.normal.append(temp)
            temp = []

        return self.normal
