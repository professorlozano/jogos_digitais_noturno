class Tank(object):
    def __init__(self, name):
        self.name = name    #nome do tanque
        self.alive = True   #para saber se o tanque está vivo ou não
        self.ammo = 5       #para armazenar a munição do tanque
        self.armor = 60     #para armazenar a armadura do tanque

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")
    
    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def fire_at(self, enemy):
        if self.ammo >=1: #verifica a qtde de balas
            self.ammo -=1 #subtrai uma bala ref a um tiro
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

tanque1 = Tank("Tank1")
tanque2 = Tank("Tank2")
tanque3 = Tank("Tank3")
tanque4 = Tank("Tank4")
tanque5 = Tank("Tank5")

array = [tanque1, tanque2, tanque3, tanque4, tanque5]

for tanque in array:
    print(tanque)



