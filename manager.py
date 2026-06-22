import re

class Manage:
    def receiver(self):
        print("Example data:(python, beginner, easy, hard python)")
        choice=input("Enter your Query:").lower()
        mapping={
            'easy':"1",
            "medium":'2',
            'hard':'3',
            'extreme':'4'
        }
        for k, v in mapping.items():
            choice=choice.replace(k,v)
        keywords=re.split(r"[,\s]+",choice.strip())
        return keywords
    def sort(self,data):
        result=data.sort_values(by="score",ascending=False).head(5)
        output=result['name'].to_string(index=False)
        return output
