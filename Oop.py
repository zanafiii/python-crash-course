class Apple:
    def __init__(self, color, flavor):
        """ Initialize the object with constructor """
        self.color = color
        self.flavor = flavor
    def __str__(self):
        """ print something when you want if the object called """
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
    
jonagold = Apple("Red", "Sweet")
print(jonagold)
help(jonagold)
    
