import random

food_dict = {'каша': 'porridge',
             'паста': 'pasta', 
             'пицца': 'pizza', 
             'сыр': 'cheese', 
             'овощи': 'vegetables', 
             'фрукты': 'fruit', 
             'суп': 'soup', 
             'салат': 'salad', 
             'хлеб': 'bread', 
             'суши': 'sushi', 
             'мясо': 'meat'}
print(f"""
Hello! Let's talk about your food preferences.
First, study the list of words for food in Russian.\n
Food in Russian:
""")
[print(key,'-',value) for key, value in food_dict.items()]


r_1 = "\nЯ люблю"
r_2 = "\nЯ обожаю"
r_3 = "\nЯ ненавижу"
r_4 = "\nЯ не люблю"
response_list = [r_1, r_2, r_3, r_4]

def Accusative(user_food):
    if user_food[-1] == "а":
        print (f"{random.choice(response_list)} {user_food[:-1]}у. А Вы?")
        user_reply = input("\nPlease reply beginning with 'Я (не) люблю', 'Я обожаю' or 'Я ненавижу:\n\n").lower()
        if user_reply[-1] != "у":
            print("\nIf you love something that ends in 'а' you need to change it to 'у'")
        else:
            print("\nThat's right, if you love something that ends in 'а' you need to change it to 'у'.")
    elif user_food[-1] == "я":
        print (f"{random.choice(response_list)} {user_food[:-1]}ю. А Вы?")
        user_reply = input("\nPlease reply beginning with 'Я (не) люблю', 'Я обожаю' or 'Я ненавижу:\n\n").lower()
        if user_reply[-1] != "ю":
            print("\nIf you love something that ends in 'я' you need to change it to 'ю'.")
        else:
            print("\nThat's right, if you love something that ends in 'я' you need to change it to 'ю'.")
    else:
        print (f"{random.choice(response_list)} {user_food}. А Вы?")
        user_reply = input("\nPlease reply beginning with 'Я (не) люблю', 'Я обожаю' or 'Я ненавижу:\n\n").lower()
        if user_reply[-1] != user_food[-1]:
            print ("\nYou don't need to change the ending if the food you like or hate doesn't end in 'а' or 'я'.")
        else:
            print ("\nGreat! Now I know what I can cook for you :)")
  

while True:
    user_food = input("\nNow type an item from the list or enter 0 to exit: ").lower()
    if user_food == "0":
        break
    elif user_food not in food_dict:
        print("\nThat's not in the list. Your choice is limited today!")
    else:
        Accusative(user_food)
    