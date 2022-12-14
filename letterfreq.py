import string, argparse

# Parsing file argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", dest="filename", type=str, required=True)
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

# Pretty printing out results
print(f"Total chars: {text_lenght}")
print("==================")
for key, value in lista.items():
    print(f"{key} -> {value}%")
