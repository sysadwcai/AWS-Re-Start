Dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 1000: "one thousand"
        }

numInput = int(input("Please enter a number."))


def numName():
    if numInput > 1000 or numInput < 0:
        print(-1)

    else:
        for k, v in dict.items():
            if k = numInput:
            print(v)

        else:
            print("one thousand")


numName()
