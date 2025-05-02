from datetime import datetime

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender        
        self.receiver = receiver  
        self.amount = amount        
        self.timestamp = datetime.now() 
