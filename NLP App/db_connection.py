import json

class Database:
    def add(self,name,email,password):
        with open('db.json','r') as f:
            data=json.load(f)
        if email in data:
            return 0
        else:
            data[email]=[name,password]
            with open('db.json','w') as wf:
                json.dump(data,wf)
            return 1

    def search(self,email,password):
        with open('db.json','r') as f:
            data=json.load(f)
            if email in data:
                if password==data[email][1]:
                    return 1
                else:
                    return 0
            else:
                return 0