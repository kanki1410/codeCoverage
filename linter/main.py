class Subway:
    def __init__(self, sauce_preference, bread_preference, onions = False, olives = False):
        self.sauce = sauce_preference
        self.bread = bread_preference
        self.onions = onions
        self.olives = olives

    def choose_sauce(self, preference):
        '''
        Choose sauce for customer
        :param preference:
        :return:
        '''
        sauce = {
            "common" : "Mayo",
            "tangy" : "Mustard",
            "spicy" : "red chillie",
            "sweet" : "sweet onion"
        }
        return (sauce["common"], sauce.get(preference, None))

    def create_sub(self):
        '''
        Create Sandwhich
        :return:
        '''
        sauce = self.choose_sauce(self.sauce)
        bread = "multigrain" # sorry we are running out of all other breads
        print(sauce)
        return sauce
        
if __name__ == "__main__":
    sub = Subway("tangy", "Ginger")
    sauce = sub.create_sub()
    print(sauce)
