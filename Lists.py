# Enumerate
winners = ["Ahmad", "Azzam", "Alhanafi"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))

# List comprehensin with condition
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [ oldname.replace(".hpp", ".h") if oldname[-4:]==".hpp" else oldname for oldname in filenames]  
print(newfilenames) 

# Dictionary
def count_letters(text):
    result = {} # Initialize the dictionary
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("azzam"))

# Update
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
