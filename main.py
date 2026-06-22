from scorer import Score
from manager import Manage

class Home:
    def __init__(self):
        self.score=Score()
        self.manage=Manage()
    def interface(self):
        keywords=self.manage.receiver()
        data=self.score.label_score(keywords)
        result=self.manage.sort(data)
        print("="*36)
        print("MATCH RESULTS")
        print("="*36)
        print(f"\n{result}")

if __name__ == "__main__":
    Home().interface()