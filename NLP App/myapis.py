import nlpcloud


class API:
    def __init__(self):
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", "421399e493f1ae0d1c19a751e86c30fba3e2e2c2", gpu=False)
    
    def sentiment_analysis(self,text):
        res=self.client.sentiment(text)
        return res
