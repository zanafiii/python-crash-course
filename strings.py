# strip
say = " yes "
print(say)
print(say.strip())      # Remove all whitespace
print(say.lstrip())     # Remove all whitespace on the left
print(say.rstrip())     # Remove all whitespace on the right

# Count, endwith, upper, lower
name = "azzam"
print(name.count("a"))          # How many times the character appears
print(name.endswith("zam"))     # Check if the end of string contains the substring
print(name.upper())             # Uppercase
print("Azzam".lower())          # Lowercase

# Join
joined = "...".join(["This", "is", "a", "phrase", "joined", "by", "thriple", "dots"])
print(joined)

# Split
splitted = "This phrase will be splitted to a string list".split()
print(splitted)

# isnumeric
print("word".isnumeric())
print("0123".isnumeric())

# formatting
def toCelcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    # The >3 is to allign the string to right by 3. The .2f is to print 2 number after dot.
    print("{:>3} F | {:>6.2f} C".format(x, toCelcius(x)))


