number_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

number = int(input())

if number in number_dict.keys():
    print(number_dict[number])
else:
    print(f"number too big")
