class Buyer():
    def __init__(self, name, type, kol, summ, price):
        self.__name = name
        self.__type = type
        self.__summ = summ
        self.__price = price
        self.__kol = kol

    def getType(self):
        return self.__type

    def getName(self):
        return self.__name

    def getSumm(self):
        return self.__summ

    def getPrice(self):
        return self.__price

    def getKol(self):
        return self.__kol

list1 = []

def add_unit_to_list(name, type, kol, price):
    list1.append(Buyer(name, type, kol, int(kol)*int(price), price))

def sort_list(key, list):
    new_list = []
    point = 0
    if key == 'summ':
        for k in range(len(list)):
            max = 0
            for i in list:
                if int(i.getSumm()) >= max:
                    point = i
                    max = int(i.getSumm())
            new_list.append(point)
            list.remove(point)
    else:
        for k in range(len(list)):
            max = 0
            for i in list:
                if int(i.getPrice()) >= max:
                    point = i
                    max = int(i.getPrice())
            new_list.append(point)
            list.remove(point)
    global list1
    list1 = new_list




