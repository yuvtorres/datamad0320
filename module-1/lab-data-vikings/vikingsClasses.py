
# Soldier


class Soldier:
    def __init__(self,d_health,d_strength):
        self.health=d_health
        self.strength=d_strength

    def attack(self):
        return self.strength

    def receiveDamage(self,d_damage):
        self.health=self.health-d_damage

# Viking

class Viking(Soldier):
    def __init__(self,d_name,d_health,d_strength):
        super().__init__(d_health,d_strength)
        self.name=d_name

    def __del__(self):
        return f"{self.name} has died in act of combat"
 
    def receiveDamage(self,d_damage):
        if self.health-d_damage<=0:
            self.health=0
            return f"{self.name} has died in act of combat"
        else:
            self.health=self.health-d_damage
            return f"{self.name} has received {d_damage} points of damage"

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
     def __init__(self,d_health,d_strength):
        super().__init__(d_health,d_strength)

     def __del__(self):
        return "A Saxon has died in combat"

     def receiveDamage(self,d_damage):
        if self.health-d_damage<=0:
            self.health=0
            return f"A Saxon has died in combat"
        else:
            self.health=self.health-d_damage
            return f"A Saxon has received {d_damage} points of damage"

  

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        self._showStatus=""

    def showStatus(self):
        if len(self.vikingArmy)!=0 and len(self.saxonArmy)!=0 :
            self._showStatus="Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy)==0:
            self._showStatus="Vikings have won the war of the century!"

        elif len(self.vikingArmy)==0:
            self._showStatus="Saxons have fought for their lives and survive another day..."

        return self._showStatus

    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
         self.saxonArmy.append(saxon)

    def vikingAttack(self):
        numsaxons=len(self.saxonArmy)
        numvikings=len(self.vikingArmy)
        result=self.saxonArmy[numsaxons-1].receiveDamage(self.vikingArmy[numvikings-1].strength)
        if self.saxonArmy[numsaxons-1].health==0:
            if numsaxons==1:
                self.saxonArmy.clear()
                self.vikingStatus="Vikings have won the war of the century!"
                return 'A Saxon has died in combat'
            else:
                del self.saxonArmy[numsaxons-1]
        else:
            return result

    def saxonAttack(self):
        numsaxons=len(self.saxonArmy)
        numvikings=len(self.vikingArmy)
        result=self.vikingArmy[numvikings-1].receiveDamage(self.saxonArmy[numsaxons-1].strength)
        if self.vikingArmy[numvikings-1].health==0:
            if numvikings==1:
                name_last_viking=self.vikingArmy[0].name
                self.vikingArmy.clear()
                return f"{name_last_viking} has died in act of combat"
            else:
                del self.vikingArmy[numvikings-1]
        else:
            return result
