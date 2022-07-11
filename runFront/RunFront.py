from datetime import datetime

class RunFronter:

    def __init__(self, brokerTrade, electronicTrade):
        self.brokerTradeId = brokerTrade.tradeId
        self.electronicTradeId = electronicTrade.tradeId
        self.electronicTimestamp = electronicTrade.time

    def __lt__(self, other):
        t1 = datetime.strptime(self.electronicTimestamp, "%H:%M:%S")
        t2 = datetime.strptime(other.electronicTimestamp, "%H:%M:%S")
        return t1 < t2

    def __eq__(self, other):
        t1 = datetime.strptime(self.electronicTimestamp, "%H:%M:%S")
        t2 = datetime.strptime(other.electronicTimestamp, "%H:%M:%S")
        return t1 == t2

    def __str__(self):
        return '({}, {})'.format(self.brokerTradeId, self.electronicTradeId)
