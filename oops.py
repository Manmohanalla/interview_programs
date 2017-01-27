class Waiter():

    def get_me_a(self, dish_name):
        dish = Dish(dish_name)
        return dish

class Dish():
    def __init__(self,dish):
        self.dish_name = dish

    def what_are_you(self):
        if 'pizza' in self.dish_name:
            pizza_type = self.dish_name.split()[:-1]
            pizza_type = ' '.join(pizza_type)
            print "I am a pizza with %s" %pizza_type
        if 'glass' in self.dish_name:
            glass_of = self.dish_name.split()[2:]
            glass_of = ' '.join(glass_of)
            print "I am a glass, filled with %s" %glass_of


waiter = Waiter()
dish = waiter.get_me_a("pepperoni pizza")   # template: {topping} pizza
dish.what_are_you()
# prints: I am a pizza with pepperoni  (I am a pizza with {topping})

dish = waiter.get_me_a("glass of mango pulp")   #template: glass of {drink}
dish.what_are_you()
# prints: I am a glass, filled with water (I am a glass, filled with {drink})