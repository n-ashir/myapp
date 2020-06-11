#import pickle library
import pickle
#from Functions import data, users

def save_recipe_data(data):
    with open('data.pkl', 'wb') as handle:
        pickle.dump(data, handle)

def read_recipe_data():
    with open('data.pkl', 'rb') as handle:
        recipe_data = pickle.loads(handle.read())
    return recipe_data

def save_login_pass (user):
    with open('log_pass.pkl', 'wb') as handle:
        pickle.dump(user, handle)

def read_login_pass():
    with open('log_pass.pkl', 'rb') as handle:
        user_and_pass = pickle.loads(handle.read())
    return user_and_pass


data = read_recipe_data()

users = read_login_pass()

print('\n Welcome to The Recipe Book.')
print("""
Open an Account, Please enter 'n' or 'new'
Login an Account, Please enter 'l' or 'login'
Continue as a Guest, Please enter 'g' or 'guest' 
""")
status = input('Please input here: ')
status = str(status)
new_user = ['new','n']
login_user = ['login', 'l']
guest_user = ['g', 'guest']
all_user = new_user + login_user + guest_user
while status not in  all_user:
    print("""\n
      Open an Account, Please enter 'n' or 'new'
      Login an Account, Please enter 'l' or 'login'
      Continue as a Guest, Please enter 'g' or 'guest' 
      """)
    status = input('Please input here: ')
if status in login_user:
   login = input('Enter login name: ').lower()
   passw = input('Enter password: ').lower()
   while login not in users:# and (users[login] != passw):
       print("\nUser doesn't exist or wrong password!\n")
       login = input('Enter login name: ').lower()
       passw = input('Enter password: ').lower()
   if login in users and users[login] == passw:
      print('\nLogin successful!\n')

elif status in new_user:
     createLogin = input("\nCreate login name: ").lower()
     if createLogin in users:
        print("\nLogin name already exist!\n")
     else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        save_login_pass(users)

elif status in guest_user:
     print('As a guest, login name: \'guest\' pass: \'guest\'!')
     print('')
     login = input('Enter login name: ').lower()
     passw = input('Enter password: ').lower()
     while not (login == 'guest' and passw == 'guest'):
            print("\nUser doesn't exist or wrong password!\n")
            print('\nPlease enter as a Guest, for login name: \'guest\' and  passw: \'guest\'!')
            login = input('Enter login name: ')
            passw = input('Enter password: ')
     else:
            print('\nLogin successful!')
name_of_food =[]
for key in data:
    name_of_food.append(key.lower())
premium = new_user + login_user
if status in guest_user:
    print("""
    As a Guest, you have only searching :
       by Categories: Like VEGAN, VEGETARIAN, NORMAL, FITNESS,Please type Category.
       by Meal Type: Like BREAKFAST, LUNCH, DINNER, SALAD, DESSERT, SNACK, Please type Meal Type.
       by Name of Recipe: Like Penne Pasta, Masala Rice, Please type name of food.       
       """)

elif status in  premium:

    print("""
    As a premium Acount owner, you can  
    Search by Categories: Like VEGAN, VEGETARIAN, NORMAL, FITNESS,Please type Category.
    Search by Meal Type: Like BREAKFAST, LUNCH, DINNER, SALAD, DESSERT, SNACK, Please type Meal Type.
    Search by Name of Recipe: Like Penne Pasta, Masala Rice, Please type name of food.
    Search Advance  like Ingredients or Calories, Please type: ADVANCED. 
    or
    Rate Recipe   : rate
    Add Recipe    : add
    Update Recipe : up
    Delete Recipe : del
     """)

    search = input('\nPlease type here: ').lower()
    #search = str(search)
    c_m_t = ['vegan', 'vegetarian', 'normal', 'fitness', 'breakfast', 'lunch', 'dinner', 'salad', 'dessert', 'snack']
    adv = ['advanced']
    joinedList = c_m_t + name_of_food + adv
    while search not in joinedList:
         print('\nUnfortunately, ' + search.title() + ' not found.')
         search = input('\nPlease search other food name or by category, by meal type: ').lower()
    if search in c_m_t  :
        for key in data:
            category_meal_type = data[key][0:2]
            for each in category_meal_type:
                if search in each:
                    result = key
                    print('\n'+ result)
    elif search in name_of_food:
         result = search.title()
         print(result)

    elif search.lower() == 'advanced' and status in premium:
        type_ing_cal = input("\nPlease type your ingredient or calorie: ", )
        if type_ing_cal.isalpha():
            var = [spl for key in data for ingre in data[key][2] for eachList in ingre for spl in ingre]
            var = ' '.join(map(str, var))
            while type_ing_cal not in var.lower():
                  print('\n'+"'"+type_ing_cal+"'",' not found. Please try again.')
                  type_ing_cal = input('Please type your ingredient: ', )
            foodName = []
            for key in data:
                for list in data[key][2]:
                    for eachlist in list:
                        spl = eachlist.split(' ')
                        for sear in spl:
                            if type_ing_cal in sear:
                                if key not in foodName:
                                   foodName.append(key)
            print('Founded Recipes: ', '\n','\n'.join(map(str, foodName)))

        elif type_ing_cal.isnumeric():
            for key in data:
                cal = data[key][3]
                if cal['calories'] <= type_ing_cal:
                    print('\nPreparing from '+type_ing_cal+' less than and equal Calories Recipes.')
                    print(key,'has ', cal['calories'], 'calories.' )
print('')
food = input('Please select one of them and past here: ')
print('Selected Recipe: ', food)
print("""
To See Ingredients, press: 2
To See Nutritious,  press: 3
To See Directions,  press: 4

To See All,         press: all

To Update,          press: up
To Delete,          press: del

To Add New Recipe   press: add
""")
asd = input('Please type here: ', )
if (asd.isnumeric() and asd == '3') and status in premium:
    print('\nPreparing ' + food + "\'s nutritioun...")
    nutri = data[food][int(asd)]
    for dictValue in nutri:
        print(dictValue.capitalize(),':',nutri[dictValue])
elif (asd.isnumeric() and asd == '2') and status in premium:
    print('\nPreparing ' + food + "\'s ingredients...")
    ingre = data[food][int(asd)]
    for listEl in ingre:
        for x in listEl:
            print(x)
elif (asd.isnumeric() and asd == '4') and status in premium:
    print('\nPreparing ' + food+"\'s direction...")
    direct = data[food][int(asd)]
    for i in direct:
        print(i)
elif (asd.isalpha() and asd == 'all') and status in premium:
     category = data[food][0]
     meal_type = data[food][1]
     ingr = data[food][2]
     nutr = data[food][3]
     direct = data[food][4]
     print('Category: ',category )
     print('Meal Type: ',meal_type)
     print('Ingredients: ', [x for each in ingr for x in each])
     print('Nutritious: ', nutr )
     print('Directions: ', direct)
elif asd.isalpha() and asd == 'del' and status in premium:
     del data[food]
     save_recipe_data(data)
     print(data[food])

elif asdisalpha() and asd == 'up' and status in premium:
     print("""
     Update Recipe
     by Category,    press 0
     by Meal Type,   press 1
     by Ingredients, press 2
     by Nutritious,  press 3
     by Directions,  press 4
     """)
     update = input('What would you update? Please input here: ', )
     if update.isnumeric() and (update == 0 or update == 1):
         cat_mel = input('Please Type your Category or Meal Type, like vegan, vegetarian or lunch, dinner')
         date[food][int(update)] = [cat_meal]
         save_recipe_data(data)
     elif update.isnumeric() and update == 2:
         print('Please Type Your Ingredients with comma. Like, 1 cup non dairy milk, 1 tablespoon apple cider vinegar')
         ingredient = input('Type here please: ',)
     elif update.isnumeric() and update == 3:
         print('Type your Nutritious, Like calories: 139, fat: 6g, Cholesterol: 212.5mg, Sodium: 195.5mg')
         my_d = input('Please input here: ')
         my_d = my_d.split(',')
         my_dict = {}
         for x in my_d:
             spl = x.split(':')
             my_dict[spl[0]] = spl[1]
         data[food][int(update)] = my_dict
         save_recipe_data(data)
     elif update.isnumeric() and update == 4:
         direct = input('Type Directions ', )
         data[food][4] = direct
         save_recipe_data(data)
elif asd.isalpha() and asd == 'add' and status in premium:
    recipe_name = input('Please type name of Recipe: ')
    data[recipe_name] = [[],[],[],{},[]]
    cat_mel = input('Please Type your Category, like vegan, vegetarian. ')
    data[recipe_name][0] = [cat_mel]
    save_recipe_data(data)
    typ_mel = input('Please Type Meal Type, like lunch, dinner. ')
    data[recipe_name][1] = [typ_mel]
    save_recipe_data(data)
    print('Please Type Your Ingredients with comma. Like, 1 cup non dairy milk, 1 tablespoon apple cider vinegar')
    ingredient = input('Type here please: ')
    ingredient = ingredient.split(',')
    add_ing =[[x] for x in ingredient]
    data[recipe_name][2] = add_ing
    print('Type your Nutritious, Like calories: 139, fat: 6g, Cholesterol: 212.5mg, Sodium: 195.5mg')
    my_d = input('Please input here: ')
    my_d = my_d.split(',')
    my_dict = {}
    for x in my_d:
         spl = x.split(':')
         my_dict[spl[0]] = spl[1]
    data[recipe_name][3] = my_dict
    save_recipe_data(data)
    direct = input('Type Directions ', )
    data[recipe_name][4] = [direct]
    save_recipe_data(data)


# search by name and RATE

    #add recipies

'''
print(
    short briefing:
    Recipe Book's Category consist of   
    VEGAN, VEGETARIAN, NORMAL, FITNESS.
    Meal Type consist of 
    BREAKFAST, LUNCH, DINNER, SALAD, DESSERT SNACK.
    
    As a Premium user, you can not only SEARCH, UPDATE, ADD and DELETE Recipes,
    but also learn CALORIES, INGREDIENTS, DIRECTIONS.
    Additionaly, RATE Recipes.
#search = input('To Continue, Please choose one of theme above.')
if diet == 'vegan':
    for key in data.keys():
        value = data[key][0]
        if 'vegan' in value:
            print (key)
            
            
if status in ['new','n','login','l']:
    print('May I check your BMI (Body Mass Index) and suggest you some Recipes?' )
    yes_or_no = str(input('Please input y/n! ', )).lower()
    if yes_or_no == 'y':
        w = int(input("Your weight in Kilograms "), )
        h = float(input("Your height in Metres, like 1.80 ", ))
        #h= (h/100)
        bmi = w / (h * h)
        print('Your BMI is:', bmi)   # your output message
        if bmi < 18:
            print( "You are underweight")
        elif bmi > 25:
               print("\nYou are overweight")
               if status in ['login','l']:
                   print('Hey' + '"' + login.capitalize() + '"' + """
                    #Hey! We have a good news. There are some low calories Recipes,
                    #which are really delicious. Would you like to see them?  \n """)
"""

#elif status in ['n' 'new']:
#   print('Hey' +"'" + createLogin.capitalize() + "'" + """
#    We have a good news. There are some low calories Recipes,
#    which are really delicious. Would you like to see them?  \n """)
"""
    yes_or_no = str(input('Please input y/n! ', )).lower()
    if yes_or_no == 'y':
       for key in data:
           calory = data[key][3]
           calories = calory['calories']
           calories = int(calories)
           if calories < 150:
               print(key)#'Please enter your choice.')
               inpt = input('Please choose on of them. ')
               print(data[inpt])

        else:
               print("You are normal")
'''


