import pandas as pd
import os 

class Score:
    def read(self):
        base = os.path.dirname(__file__)
        path = os.path.join(base, "project.csv")
        return pd.read_csv(path)
    def counter(self,keywords,row):
        score=0
        for keys in keywords:
            if keys in row['description']:
                score+=3
            if keys in row["tags"]:
                score+=4
            if keys==str(row['difficulty']):
                score+=2
        return score
    def label_score(self,keywords):
        data=self.read()
        data['score']=data.apply(lambda row: self.counter(keywords,row),axis=1)  
        return data



        

