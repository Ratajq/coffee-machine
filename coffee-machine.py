class MyCoffee:
    water = 400
    milk = 540
    coffee_b = 120
    cups = 9
    money = 550
    state = 'menu'
    end = 1 #ending condiotion
    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_b} of coffeee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')
        return
    def buy_esp(self):
        self.state = 'menu'
        res = [self.water, self.coffee_b, self.cups]
        res_name = ['water', 'coffee beans', 'cups']
        esp_ing = [250, 16, 1]
        for i in range(len(res)):
            if res[i] < esp_ing[i]:
                print('Sorry, not enough', res_name[i]+'!')
                break
            i += 1
        else:
            self.water -= 250
            self.coffee_b -= 16
            self.cups -= 1
            self.money += 4
            print('I have enough resources, making you a coffee!')
            return
    def buy_lat(self):
            self.state = 'menu'
            res = [self.water, self.milk, self.coffee_b, self.cups]
            res_name = ['water', 'milk', 'coffee beans', 'cups']
            lat_ing = [350, 75, 20, 1]
            for i in range(len(res)):
                if res[i] < lat_ing[i]:
                    print('Sorry, not enough', res_name[i]+'!')
                    break
                i += 1
            else:
                self.water -= 350
                self.coffee_b -= 20
                self.milk -= 75
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
    def buy_cap(self):
        self.state = 'menu'
        res = [self.water, self.milk, self.coffee_b, self.cups]
        res_name = ['water', 'milk', 'coffee beans', 'cups']
        cap_ing = [200, 100, 12, 1]
        for i in range(len(res)):
            if res[i] < cap_ing[i]:
                print('Sorry, not enough', res_name[i]+'!')
                break
            i += 1
        else:
            self.water -= 200
            self.milk -= 100
            self.coffee_b -= 12
            self.cups -= 1
            self.money += 6
            print('I have enough resources, making you a coffee!')
        return
    def back(self):
        self.state = 'menu'
        return
    def fill(self):
        global water, milk, coffee_b, cups, money
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_b += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
        return
    def take(self):
        print('I gave you $', self.money)
        self.money = 0
    def buy(self):
        self.state = 'buy'
    def  back(self):
        self.state = 'menu'
    def exit(self):
        self.end = 0
    def start(self):
        while (self.end != 0):
            if self.state == 'menu':
                print('Write action (buy, fill, take, remaining, exit):')
                action = input()
                if action == 'buy': self.buy()
                elif action == 'fill': self.fill()
                elif action == 'take': self.take()
                elif action == 'remaining': self.remaining()
                elif action == 'exit': self.exit()
                else: print('wrong aciton!')
            else:
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                action = input()
                if action == '1': self.buy_esp()
                elif action == '2': self.buy_lat()
                elif action == '3': self.buy_cap()
                elif action == 'back': self.back()
                else: print('wrong action!')

MyCoffee().start()






