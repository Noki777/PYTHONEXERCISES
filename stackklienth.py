class Stack:
    def __init__(self):
        print ("LIST MANIPULATION USING STACK")
        self.items = input("\nEnter a list of strings:")
        self.items = list(self.items)

    def sort(self):
        return sorted(self.items)

    def reverse(self):
        return self.items[::-1]

    def isEmpty(self):
        return self.items == []

    def insert(self,value,item):
        return self.items.insert(value,item)

    def push(self, item):
        return self.items.append(item)

    def append(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    noki = Stack()
    def qt():

        nokii = 0
        print ("\n1. SORT THE LIST \n2. REVERSE THE LIST \n3. ADD AN ITEM \n4. INSERT AN ITEM \n5. GET THE SIZE \n6. COUNT THE PALINDROME")
        x = input("\nChoose the action you want: ")
        if x == 1:
            print ("SORTED VERSION: "),noki.sort()
        elif x == 2:
            nokiii = []
            while noki.isEmpty() == False:
                nokiii.append(noki.peek())
                noki.pop()
            print ("REVERSED VERSION:"), nokii
            return 0

        elif x == 3:
            nokiiii = input("\tEnter the word you wanna add: ")
            GF.push(nokiiii)
            print ("\t"), noki.items
        elif x == 4:
            nokiiii = input("\tInsert: ")
            noki1 = input("\tIndex: ")
            noki.insert(noki1, nokiiii)
            print ("\t"),noki.items
        elif x == 5:
            print ("SIZE:"),noki.size()
        elif x == 6:
            while noki.isEmpty() == False:
                if noki.peek() == noki.peek()[::-1]:
                    nokii += 1
                noki.pop()
            print ("TOTAL PALINDROME: "), nokii
            return 0


        return qt()
    qt()