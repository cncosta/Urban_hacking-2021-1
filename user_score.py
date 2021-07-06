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
    def __init__(self):
        
        self.u_yes = 0 # aumenta cada vez que reconoce correctamente la diferencia
        self.u_no = 0 # aumenta cada vez que reconoce incorrectamente la diferencia
        
        self.u_ia = 0 # cantidad de plata que gasta en arte de ia.  
        self.u_human = 0 #cantidad de plata que gasta en arte humano.

    def general_result(self):
        if self.yes > self.no:
            '''
            El usuario reconce en su mayoria el origen de la obra 
            '''
            if self._ia < self.human: # el usuario valora más el arte humano. 
                pass
            elif self._ia > self.human: # el usuario valora más el arte artificial
                pass
            elif self._ia == self.human: # valora por igual ambos artes
                pass

    
        elif self.yes < self.no:
            '''
            El usuario no reconce en su mayoria el origen de la obra 
            '''
            pass

        
        elif self.yes == self.no:
            pass


    def user_result(self):
        if self.u_yes > self.u_no:
            '''
            El usuario reconce en su mayoria el origen de la obra 
            '''
            if self._ia < self.human: # el usuario valora más el arte humano. 
                pass
            elif self._ia > self.human: # el usuario valora más el arte artificial
                pass
            elif self._ia == self.human: # valora por igual ambos artes
                pass

    
        elif self.u_yes < self.u_no:
            '''
            El usuario no reconce en su mayoria el origen de la obra 
            '''
            pass

        elif self.u_yes == self.u_no:
            pass
        

        

