fruit = input()
day = input()
quality = float(input())

fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
price_dict = {
    "week": {
        "banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
    },
    "weekend": {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.60,
        "grapes": 4.20
    }
}

if day in week and fruit in fruits:
    value = price_dict["week"][fruit] * quality
    print(f"{value:.2f}")
elif day in weekend and fruit in fruits:
    value = price_dict["weekend"][fruit] * quality
    print(f"{value:.2f}")
else:
    print(f"error")
