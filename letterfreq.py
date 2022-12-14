import string, argparse

# Parsing file argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", dest="filename", type=str, required=True)
parser.add_argument("--plot", dest="plot", action="store_true")
args = parser.parse_args()

# Opening text file specified
try:
    with open(args.filename) as f:
        text = f.read()
except FileNotFoundError:
    print("File not found!")
    exit(1)

# We need only lowercase letters
text = text.lower()

# Removing all useless whitespaces and symbols
for letter in text:
    if letter not in string.ascii_lowercase:
        text = text.replace(letter, "")

# Printing total text lenght
text_lenght = len(text)

# Defining an empty list to append results
lista = {}

# Counting every occurence of letters in our text
for letter in string.ascii_lowercase:
    total = text.count(letter)
    percent = round((total*100)/text_lenght, 3)
    lista.update({letter: percent})

# Now Sorting results
lista = dict(sorted(lista.items(), key=lambda item: item[1], reverse=True))

# If we choose to not plot
if not args.plot:

    # Pretty printing out results
    print(f"Total chars: {text_lenght}")
    print("==================")

    for key, value in lista.items():
        print(f"{key} -> {value}%")
    
    exit(0)


# If we choose to plot
if args.plot:

    import matplotlib.pyplot as plt

    # Italian frequency distribution
    italian = {'e': 11.49, 'a': 10.85, 'i': 10.18, 'o': 9.97, 'n': 7.02, 't': 6.97, 'r': 6.19, 'l': 5.70, 's': 5.48, 'c': 4.30, 'd': 3.39, 'u': 3.16, 'p': 2.96, 'm': 2.87, 'v': 1.75, 'g': 1.65, 'h': 1.43, 'b': 1.05, 'f': 1.01, 'z': 0.85, 'q': 0.45}

    # The following lines are used to sort the lists by keys
    risultante1 = {}
    risultante2 = {}

    for key, value in lista.items():
        for key1, value1 in italian.items():
            if key == key1:
                risultante1.update({key: value})
                risultante2.update({key: value1})

    # Now we plot
    plt.scatter(risultante1.keys(), risultante1.values(), color='red')
    plt.scatter(risultante1.keys(), risultante2.values(), color='green')
    plt.suptitle(f" {args.filename} compared against italian frequency distribution")
    plt.legend(title='Legend', labels=["Italian", "File"])
    plt.show()
