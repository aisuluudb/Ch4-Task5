# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

class Soldier():
    def __init__(self, name):
        self.name = name

        

class Guns():
    def __init__(self, bullets=10):
        self.bullets = bullets
        

    def bulleting(self):
        for _ in range(self.bullets):
            print('tigi-tigitishh')
            self.bullets -= 1
        
        
    def reload(self):
        self.bullets = 10
        print('Reloading')
        

      

class ActofShooting(Soldier, Guns):
    def __init__(self, name, bullets, value):
        Soldier.__init__(self, name)
        Guns.__init__(self, bullets)
        self.value = value
    
    def shoot(self):
        self.bulleting()
        self.reload()
        self.bulleting()



shooting = ActofShooting('Rayan', 10)
print(shooting.shoot())

