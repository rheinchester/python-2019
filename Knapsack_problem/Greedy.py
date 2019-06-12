class Food(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.calories = weight
    
    def getValue (self):
        return self.value
    
    def getCalories (self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCalories()

    def __str__(self):
        return self.name+': <'+ str(self.value)\
            +', '+str(self.calories)+'>'


def buildMenu(names, values, calories):
    '''
        Return list of foods
        (why  must it be len(values))
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """Key function maps elements of items to numbers
    """
    result = []
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    totalValue , totalCalories = 0.0, 0.0
    for i in range(len(itemsCopy)):
        item = itemsCopy[i]
        if (totalCalories + item.getCalories()) <= maxCost:
            result.append(item)
            totalCalories += item.getCalories()
            totalValue += item.getValue()
    return result, totalValue



def testGreedy (items, constraint, keyFunction, param):
    # taken returns a list of items with a total value val
    taken, val = greedy(items, constraint, keyFunction)
    print('total value of taken items by ',param, ' = ', val)
    for item in taken:
        print(' ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue, 'value')
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCalories(x), 'calories')
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density, 'density')


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)

