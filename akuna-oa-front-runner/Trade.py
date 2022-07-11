from datetime import datetime

class Trade:
    def __init__(self, date, time, type, qty, strike, expiry, kind, exchange, tradeId, product, side=None):
        self.date = date
        self.time = time
        self.type = type
        self.qty = qty
        self.strike = strike
        self.expiry = expiry
        self.kind = kind
        self.exchange = exchange
        self.tradeId = tradeId
        self.product = product
        self.side = side

    def isWithinOneMinute(self, anotherTrade):
        t1 = datetime.strptime(self.time, "%H:%M:%S")
        t2 = datetime.strptime(anotherTrade.time, "%H:%M:%S")
        delta = t1 - t2
        return 0 <= delta.total_seconds() <= 60

    def isFrontRunner(self, anotherTrade):
        if self.type == anotherTrade.type:
            return False
        if not self.isWithinOneMinute(anotherTrade):
            return False
        if self.product != anotherTrade.product:
            return False
        if self.kind != anotherTrade.kind:
            return False
        if self.exchange == 'CBOE':
            if (self.qty < 0 and anotherTrade.qty >= 0) or (self.qty >= 0 and anotherTrade.qty < 0):
                return False
        else:
            if self.side != anotherTrade.side:
                return False
        if self.expiry != anotherTrade.expiry:
            return False
        if self.strike != anotherTrade.strike:
            return False

        # All conditions have been met for the front runner
        return True