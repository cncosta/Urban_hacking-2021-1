'''
En este código se calcula el puntaje del usuario
este puntaje es cuantas veces pudo diferenciar el arte artificial v/s
el humano y que tanto valoró el arte artificial v/s el arte humano. 
'''
class User:
    yes = 0 # aumenta cada vez que reconoce correctamente la diferencia
    no = 0 # aumenta cada vez que reconoce incorrectamente la diferencia  
    ia = 0 # cantidad de plata que gasta en arte de ia.  
    human = 0 #cantidad de plata que gasta en arte humano
    def __init__(self) -> None:
        
        self.u_yes = 0 # aumenta cada vez que reconoce correctamente la diferencia
        self.u_no = 0 # aumenta cada vez que reconoce incorrectamente la diferencia
        
        self.u_ia = 0 # cantidad de plata que gasta en arte de ia.  
        self.u_human = 0 #cantidad de plata que gasta en arte humano.

    def general_result(self) -> str:
        inicio = 'Is The year 2050, art made by '
        opcion0 = ['humans ', 'artificial inteligence']
        opcion1 = 'is the most popular'
        opcion2 = ['People know diferrence between A.I art and Human art','People dont know diferrence between A.I art and Human art']
        
        if self.yes > self.no:
            '''
            El usuario reconce en su mayoria el origen de la obra 
            '''
            if self.ia <= self.human: # el usuario valora más el arte humano. 
                return inicio + opcion0[0] + opcion1 + opcion2[0]
            
            elif self.ia > self.human: # el usuario valora más el arte artificial
                return inicio + opcion0[1] + opcion1 +opcion2[0]
            
        elif self.yes <= self.no:
            
            if self.ia <= self.human: # el usuario valora más el arte humano. 
                return inicio + opcion0[0] + opcion1 + opcion2[1]
            
            elif self.ia > self.human: # el usuario valora más el arte artificial
                return inicio + opcion0[1] + opcion1 +opcion2[1]
            

    def user_result(self)-> str:
        inicio = 'Is The year 2050, art made by '
        opcion0 = ['humans ', 'artificial inteligence']
        opcion1 = 'is the most popular.'
        opcion2 = [' People know diferrence between A.I art and Human art','People dont know diferrence between A.I art and Human art']
        
        if self.u_yes > self.u_no:
            '''
            El usuario reconce en su mayoria el origen de la obra 
            '''
            if self.u_ia <= self.u_human: # el usuario valora más el arte humano. 
                return inicio + opcion0[1] + opcion1 + opcion2[0]
            
            elif self.u_ia > self.u_human: # el usuario valora más el arte artificial
                return inicio + opcion0[0] + opcion1 +opcion2[0]


        elif self.u_yes <= self.u_no:
            
            if self.u_ia <= self.u_human: # el usuario valora más el arte humano. 
                return inicio + opcion0[1] + opcion1 + opcion2[1]
            
            elif self.u_ia > self.u_human: # el usuario valora más el arte artificial
                return inicio + opcion0[0] + opcion1 +opcion2[1]


    def __str__(self) -> str:
        txt = f'Aciertos: {self.u_yes} | monto humanos: {self.u_human} | monto A.I. {self.u_ia} \n'
        return txt

if __name__ == '__main__':
    import random as rd
    from story_tellingAPI import story_telling
    usuarios = {
    }
    for user in range(10):
        usuarios.update({user: User()})
        value_1, value_2 = rd.randint(0,100), rd.randint(0,100) 
        usuarios[user].u_yes = value_1
        usuarios[user].u_no = 100 - value_1
        usuarios[user].u_ia = value_2
        usuarios[user].u_human = 100 - value_2
        print(usuarios[user], story_telling(usuarios[user].user_result()),'\n',40*'_')
        