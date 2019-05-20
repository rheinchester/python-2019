
def greedy (items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalCost, totalValue = 0.0, 0.0 

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
