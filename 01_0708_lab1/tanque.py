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

meuTanque = Tank("Bob")
meuTanque2 = Tank("Jack")
meuTanque.fire_at(meuTanque2)
print(meuTanque)
print(meuTanque2)



