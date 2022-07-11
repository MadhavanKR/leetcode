from Trade import Trade
from FrontRunner import FrontRunner

def createInputs():
    trades = []
    trades.append(Trade('2022-03-15', '9:01:00', 'Broker', -500, 1500, '2022-04-28', 'P', 'CBOE', '737acm', 'ABC'))
    trades.append(Trade('2022-03-15', '9:00:24', 'Electronic', -200, 1500, '2022-04-28', 'P', 'CBOE', 'w6c229', 'ABC'))
    trades.append(Trade('2022-03-15', '9:00:23', 'Electronic', -200, 1500, '2022-04-28', 'P', 'CBOE', 'abcdef', 'ABC'))
    trades.append(Trade('2022-03-15', '9:03:45', 'Electronic', -100, 1500, '2022-04-28', 'P', 'CBOE', 'tssrin', 'ABC'))
    return trades


if __name__ == '__main__':
    trades = createInputs()
    tradeMap = {}

    for trade in trades:
        tradeMap[trade.tradeId] = trade

    productBucket = {} # map of products to list of broker trades

    result = []
    # populating product bucket
    for trade in trades:
        if trade.type == 'Broker':
            if trade.product not in productBucket:
                productBucket[trade.product] = []
            productBucket[trade.product].append(trade.tradeId)

    for trade in trades:
        if trade.type == 'Electronic' and trade.product in productBucket:
            for brokerTradeId in productBucket[trade.product]:
                brokerTrade = tradeMap[brokerTradeId]
                if brokerTrade.isFrontRunner(trade):
                    result.append(FrontRunner(brokerTrade, trade))
    result.sort()
    for res in result:
        print(res)
    print(result)
