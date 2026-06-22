import pandas as pd

class Score:
    def read(self):
        data=pd.read_csv("project/project.csv")
        return data
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



        

