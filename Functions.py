
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

users = {'guest':'guest'}

data = {
    'Gingerbread Waffels':
        [
            ['vegan'],
            ['breakfast', 'dessert'],
            [
                ['125g spelt flour'], ['1 tablespoon ground flax seeds'], ['2 teaspoons baking powder'],
                ['1/4 teaspoon baking soda'],
                ['1/4 teaspoon salt'], ['1.5 teaspoons ground cinnamon'], ['2 teaspoons ground ginger'],
                ['4 tablespoons coconut sugar'],
                ['1 cup non dairy milk'], ['1 tablespoon apple cider vinegar'], ['2 tablespoons black strap molasses'],
                ['1½ tablespoons liquid oil ']
            ],
            {'calories': '173', 'fat': '4.6g', 'carbohydrates': '29g', 'protein': '3.5g', 'cholesterol': '0mg',
             'sodium': '272mg', 'calcium': '220mg', 'iron': '1.6mg', 'fiber': '3.4g'},
            [
                '''1.Put all of the dry ingredients into a bowl and stir well. 
                2.Put all of the wet ingredients into a jug or bowl (one with a lip is easier to pour). Stir until well combined.
                3.Pour the mixed wet ingredients into the dry ingredients and mix using a spoon, until just combined.
                4.When your waffle iron is ready pour in your mixture until it's just full and cook on a medium temperature until steam stops coming out of the side. 
                '''
            ]
        ],
    'Baked Blueberry Muffin':
        [
            ['normal'],
            ['dessert'],
            [
                ['1 cup unsweetened cashew milk'], ['1 tablespoon ground flaxseed'], ['1 tablespoon almond meal'],
                ['1 tablespoon maple syrup'],
                ['1 teaspoon vanilla extract'], ['1 teaspoon cinnamon'], ['2 teaspoons nutritional yeast'],
                ['3/4 cup frozen blueberries'],
                ['9 slices soft bread'], ['1/4 cup oats'], ['1/3 cup raw pecans'], ['1/4 cup coconut sugar '],
                ['3 tablespoons coconut butter'], ['1/8 teaspoon sea salt']
            ],
            {'calories': '132', 'fat': '5g', 'carbohydrates': '17g', 'protein': '3g', 'potassium': '91mg',
             'calcium': '33mg', 'iron': '0.9mg', 'fiber': '3g', 'sodium': '129mg'},
            [
                '''1.Put 1 teaspoon of liquid mixture in the bottom of each muffin space.
                2.Add 1 square piece of bread.
                3.Place about 5-6 blueberries, depending on size, so that they cover the center of the bread.
                4.Sprinkle about 1/2 tablespoon of crumble topping over the blueberries.
                5.Put 1 square piece of bread over the top and use your fingers to pack it in well.
                6.Place 5-6 more blueberries on the bread.
                7.Sprinkle about 1/2 tablespoon of crumble topping over the blueberries.
                8.Put another square piece of bread over the top and use your fingers to pack it in well.
                9.Sprinkle with a little bit of the crumble topping.
                10.Carefully add 1 tablespoon of liquid mixture over the top, making sure to evenly coat so that all the bread gets soaked.
                11.Add 2-3 more blueberries on top for décor, and sprinkle with a tad of plain coconut sugar if you want.
                12.Bake for 35 minutes. Because ovens vary, start checking them at 25 minutes. They are ready when the tops begin to brown. 
                '''
            ]
        ],
    'Tofu Scramble':
        [
            ['vegetarian'],
            ['launch'],
            [
                ['2 tablespoons nutritional yeast'], ['1 teaspoon chili powder'], ['1 teaspoon ground cumin'],
                ['1 teaspoon black salt'],
                ['3/4 teaspoons turmeric'], ['1/4 teaspoon garlic powder'], ['1 tablespoon oil'],
                ['1 1/2 cups sliced mushrooms'],
                ['1 chopped red pepper'], ['1/2 yellow onion chopped'], ['2 cloves garlic'],
                ['400g block medium-firm tofu'],
                ['black beans (2 cups']
            ],
            {'calories': '175', 'fat': '9g', 'carbohydrates': '10g', 'protein': '14g', 'sodium': '600mg',
             'calcium': '152mg', 'iron': '2.6mg', 'fiber': '3g'},
            ['''1.Add all of the spice mix ingredients into a bowl and stir to combine.
2.Heat a large skillet over medium-high heat and add the olive oil. 
3.Add the mushrooms, pepper, onion, and garlic and sauté for about 8 minutes until everything just starts to brown.
4.Add the tofu blocks and break it apart with your spoon until you get a nice scramble texture with lots of chunks. 
5.Stir in the spice mix and black beans. 
6.Heat through for another 5 - 8 minutes until hot.
'''
             ]
        ],
    'Zucchini Turkey Tacos':
        [
            ['fitness'],
            ['lunch', 'dinner'],
            [
                ['4 medium zucchini'], ['1/2 cup salsa plus more for serving'], ['1 pound ground turkey'],
                ['1 teaspoon garlic powder'],
                ['1 teaspoon cumin'], ['1 teaspoon cinnamon'], ['1 teaspoon salt or to taste'],
                ['1 teaspoon chili powder'],
                ['1 teaspoon paprika'], ['1/2 small onion minced'], ['4 oz tomato sauce'],
                ['1/2 cup or so shredded Mexican cheese blend']
            ],
            {'calories': '239', 'fat': '7g', 'carbohydrates': '13g', 'protein': '34g', 'potassium': '1104mg',
             'calcium': '148mg', 'iron': '3mg', 'fiber': '4g', 'sodium': '1141mg'},
            [
                '''1.Bring a large pot of salted water to boil.
                2.Pour 1/2 cup of salsa into the bottom of a baking dish.
                3.Cut the zucchini in half lengthwise then with a small spoon or melon baller.
                4.Save 3/4 cup of the zucchini flesh and chop into small pieces.
                5.Drop the zucchini halves into the boiling water and cook for one minute, remove from water and set aside.
                6.Preheat the oven to 400 degrees.
                7.In a large skillet, brown the ground turkey, breaking it up while it cooks. 
                8.Add in the chopped onion, reserved zucchini, tomato sauce, and water. 
                9.Stir it up then cover and simmer on low for 20 minutes.
                10.Arrange the boiled zucchini halves into the bottom of the dish.
                11.Once the meat mixture is done, spoon the mixture into the zucchini boats evenly. 
                12.Top each half with a sprinkle of cheese.
                13.Cover the pan with foil and bake for approximately 30 minutes until the zucchini is fully cooked and the cheese is melted.
                14.Serve with sour cream and more salsa.
                '''
            ]
        ],
    'Black Bean Soup':
        [
            ['fitness'],
            ['lunch', 'dinner'],
            [
                ['1 medium onion'], ['1 tablespoon minced garlic'], ['2 teaspoon ground cumin'], ['1 jalapeño'],
                ['216 gram black beans'], ['1 teaspoon cinnamon'], ['115 gram diced tomatoes']
            ],
            {'calories': '245', 'fat': '0.5g', 'carbohydrates': '30g', 'protein': '15g', 'fiber': '11g'},
            [
                '''1.large pot over medium-high heat with oil.
                2.Add onion and cook until translucent.
                3.Add garlic, cumin and jalapeno and cook 1 minute more.
                4.Add beans to pot and lightly mash with a potato masher or fork.
                5.Add tomatoes and broth – bring to a boil and reduce to medium heat, cover and simmer for 15 minutes.
                '''
            ]
        ],
    'Honey Garlic Salmon':
        [
            ['fitness'],
            ['lunch', 'dinner'],
            [
                ['1 teaspoon minced garlic'], ['1/2 teaspoon minced ginger'], ['4 tablespoons honey'],
                ['2 tablespoons soy sauce'],
                ['250gr salmon filet'], ['1 teaspoon timian']
            ],
            {'calories': '440', 'fat': '14g', 'carbohydrates': '36.6g', 'protein': '45.3g', 'calcium': '9mg',
             'iron': '11mg'},
            [
                '''1.Combine the sauce ingredients and marinate the salmon in the sauce for 15-30 minutes.
                2.Arrange salmon on a foil-lined baking sheet and bake at 350 degrees F for 15-20 minutes depending on thickness.
                3.Basting the salmon with the leftover marinade halfway through. 
                4.Over medium high heat, bring the leftover marinade sauce to a boil and simmer for 3-5 minutes until reduced.
                5.Dish and serve the salmon hot drizzled with reduced sauce
                '''
            ]
        ],
    'Fresh Berry Fool':
        [
            ['normal'],
            ['dinner'],
            [
                ['1 cup fresh raspberries'], ['1 cup fresh blackberries, broken in half'],
                ['1 cup fresh strawberries, hulled and quartered'],
                ['1 teaspoon lemon zest'], ['1 teaspoon freshly squeezed lemon juice'], ['1/4 cup white sugar'],
                ['1 cup chilled heavy cream'],
                ['1/4 cup creme fraiche'], ['1 tablespoon white sugar'], ['1/4 teaspoon pure vanilla extract'],
                ['1 cup crushed shortbread cookies']
            ],
            {'calories': '646', 'fat': '41.7g', 'carbohydrates': '64.8g', 'protein': '6.3g', 'cholesterol': '113mg',
             'sodium': '287mg '},
            ['''1.Place raspberries, blackberries, and strawberries in a bowl. Add lemon zest, 
lemon juice, and 1/4 cup sugar. Stir until sugar is mixed with fruit and juices begin to form. 
Cover and refrigerate until chilled, about 1 hour.
2.Place heavy cream and creme fraiche in a cold bowl. Add 1 tablespoon sugar and vanilla extract. 
Whisk until mixture has soft peaks and sharp lines, 5 to 8 minutes.
3.Place some cookie crumbs in the bottom of each serving dish. Spoon in some of the fruit and a layer of whipped cream. 
Repeat layers, ending with a sprinkle of cookie crumbs.''']
        ],
    'Greek Salad':
        [
            ['normal', 'fitness'],
            ['salad'],
            [
                ['Sliced cucumber ¼ inch'], ['red bell pepper 1 nos'], ['cherry tomatoes, halved 10 nos'],
                ['red onion, sliced in half-rounds 1/2 nos'],
                ['feta cheese ½ inch diced '], ['olives pitted 1/2 cups'], ['dried oregano 1 tsp'],
                ['English mustard 1/2 tsp'],
                ['red wine vinegar 30 ml'], ['salt 1 tsp']
            ],
            {'calories': '179', 'fat': '15g', 'Cholesterol': '25mg', 'Sodium': '370mg', 'potassium': '238mg',
             'Total Carbohydrates': '7.4g'},
            [
                '''1.	Place the cucumber, peppers, tomatoes and red onion in a large bowl.
                2.For the vinaigrette: Whisk together the oregano, mustard, vinegar, salt and freshly ground black pepper in a small bowl.
                3.Still whisking, slowly add the garlic infused olive oil to make an emulsion.
                4.Pour the vinaigrette over the vegetables.
                5.Add the feta and olives and toss lightly.
                6.Set aside for 30 minutes to allow the flavours to blend. 
                '''
            ]
        ],
    'Penne Pasta':
        [
            ['normal'],
            ['lunch', 'dinner'],
            [
                ['pasta 2 cups'], ['onion 1 nos'], ['red yellow and green pepper cut lenghtwise 1 nos'],
                ['carrot 1 nos'],
                ['milk 1 cups'], ['butter 2 tbsp'], ['black pepper 1 tsp'], ['chat masala 1 tsp'],
                ['chilli flakes 1 tsporegano 1 tsp'], ['cloves of garlic 7-8 nos'],
                ['Grind coarsely green chillies n garlic 1 tsp'], ['Salt as per taste. 1 pinch']
            ],
            {'calories': '352', 'fat': '1.9g', 'fibre': '2.7', 'Protein': '12.4', 'Total Carbohydrates': '71.3g'},
            [
                '''1.Heat 1 tbsp butter in a pan n saute the garlic chilli paste add onion n all the vegetalbes n saute for 2_3 mins. N remove them in a plate.
                2.Now in the same pan heat butter n saute maida. Add milk n jeep stirring to avoid lumps.
                3.When ur paste gets thicken add blk pepper chilli flakes salt n oregano. N mix well .
                4.Add the sauted veges n boiled pasta. Mix well n cook for few 
                 '''
            ]
        ],
    'Vanilla Nut Cake':
        [
            ['vegan'],
            ['dessert'],
            [
                ['flour 2 cup'], ['Corn strach 3 tbsp'], ['Baking powder 1 tsp'], ['Baking soda 1 tsp'],
                ['Salt 1/4 tsp'], ['Vegetable oil 1/2 cup'], ['Vegetable oil 1/2 cup'], ['Caster sugar 1 cup'],
                ['Vanilla extract 1 tsp']
            ],
            {'calories': '421', 'fat': '19.59g', 'Cholesterol': '51mg', 'Sodium': '397mg', 'potassium': '238mg',
             'Total Carbohydrates': '59.58g', 'protein': '3.56g'},
            [
                '''
                1.In a large bowl mix all the dry ingredients like flour, corn starch, baking soda, baking powder, salt and sugar.
                2.Into the same bowl add the Mixture of water and oil along with vanilla essence.
                3.Further mix it well in cut and fold method without the hand mixer.
                4.Pour the batter into the baking tray. Top it up with roasted cashewnuts.
                5.Pre - heat the oven @ 180°c and bake it for 35 minutes.
                6.Cool the cake down completely. Best served with hot chocolate milk.
                '''
            ]
        ],
    "Bird's Nest":
        [
            ['vegetarian'],
            ['snack'],
            [
                ['Potatoes - 3 '], ['Paneer - 100 gm '], ['Corn flour - 2 tbsp'], ['Vermicelli - 1 cup'],
                ['Red chili powder - 1/2 tsp'], ['Turmeric powder - 1/4 tsp'], ['Gram masala powder - 1/4 tsp'],
                ['Oil - for frying'],
                ['Salt - to taste '], ['Coriander leaves – few']
            ],
            {'calories': '139', 'fat': '6g', 'Cholesterol': '212.5 mg', 'Sodium': '195.5mg', 'potassium': '110.6 mg',
             'Total Carbohydrates': '12.4g'},
            [
                '''1.Firstly boil, peel and mash the potatoes well. 
                2.2.Add red chilli powder, turmeric powder, garam masala powder, salt, coriander leaves, and mix well. 
                3.Make big lemon-size balls, and then into bowl shape. 
                4.Take wheat flour, add some water and make it into a thick batter (dosa-batter consistency). 
                5.Dip the potato bowls in the wheat flour batter. 
                6.Give a quick vermicelli coating to the bowls. 
                7.Set for 5 minutes. 
                8.Now heat the oil for frying, put the potato bowls carefully into the oil. 
                9.Allow to fry for 3 to 4 minutes and turn them over, till they turn golden brown. 
                10.Your yummy potato birds' nest is ready. 
                11.Take paneer and roll it into small amla-sized balls. 
                12.Deep fry the paneer balls for 1/2 min. 13.Finally decorate with paneer balls.
                
                '''
            ]
        ],
    'Masala Rice':
        [
            ['normal'],
            ['lunch', 'dinner'],
            [
                ['Cooked rice 4 cups'], ['Ginger garlic paste 2 tbsp'], ['Green chili paste 1 tsp'],
                ['Red chili powder 2 tbsp'],
                ['Salt 1 tsp or to taste'], ['Lemon juice 2 tbsp'], ['Curry leaves 1/4 th cup'],
                ['Asafetida 1/8 th tsp'],
                ['Onion thinly sliced large ones 2'], ['Oil 3 tbsp']
            ],
            {'calories': '207', 'fat': '5.4g', 'Cholesterol': '0mg', 'Sodium': '206mg', 'potassium': '224mg',
             'Total Carbohydrates': '36g'},
            [
                '''1.In a wide cooking pot, mix all the spices along with the cooked rice.
                2.Keep it aside.
                3.Also add the lemon juice to it.
                4.In a pan, heat oil and add Cumin seeds.
                5.After half a minute, add Asafetida and Curry leaves.
                6.Next, add sliced onions and saute until golden brown.
                7.Add this tempering to the rice mix and give it all a good stir.
                8.Keep this on low heat to simmer for about 15 to 20 minutes or little more.
                9.Serve hot as it is or with any pickle of choice, poppadums and ghee.
                10.This is my mom's recipe for making something quick and easily too.
                11.You can add ghee to the tempering instead of oil if desired. Garnish with coriander leaves and serve hot immediately.
                
                '''
            ]
        ]
}
#asd = input('add your Recipe: ')
if asd.isalpha() and asd == 'add':
    recipe_name = input('Please type name of Recipe: ')
    data[recipe_name] = [[],[],[],{},[]]
    #cat_mel = input('Please Type your Category, like vegan, vegetarian. ')
    data[recipe_name][0] = [cat_mel]
    #save_recipe_data(data)
    #typ_mel = input('Please Type Meal Type, like lunch, dinner. ')
    data[recipe_name][1] = [typ_mel]
    #save_recipe_data(data)
    print('Please Type Your Ingredients with comma. Like, 1 cup non dairy milk, 1 tablespoon apple cider vinegar')
    #ingredient = input('Type here please: ')
    #ingredient = ingredient.split(',')
    add_ing =[[x] for x in ingredient]
    data[recipe_name][2] = add_ing
    print('Type your Nutritious, Like calories: 139, fat: 6g, Cholesterol: 212.5mg, Sodium: 195.5mg')
    #my_d = input('Please input here: ')
    #my_d = my_d.split(',')
    my_dict = {}
    for x in my_d:
         spl = x.split(':')
         my_dict[spl[0]] = spl[1]
    data[recipe_name][3] = my_dict
    #save_recipe_data(data)
    direct = input('Type Directions ', )
    data[recipe_name][4] = [direct]

    #save_recipe_data(data)
    print(data[recipe_name])
    print(data[recipe_name][4])
