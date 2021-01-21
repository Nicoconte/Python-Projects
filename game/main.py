
import os
import time


class Game:

    map = []
    border_sprite = "@"

    width = None
    height = None

    player_sprite = "?"
    player_position = [0, 0] #y, x
    player_input = 0

    def __init__(self, height, width):
        self.width = width
        self.height = height 

    def generate_map(self):    
        
        for i in range(self.height):
            self.map.append([''] * self.width)

        return self.map

    def draw_borders(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                #Primera fila
                if i == 0:
                    self.map[0][j] = self.border_sprite

                #Ultima fila
                elif i == self.height -1:
                    self.map[i][j] = self.border_sprite

                #Filas restantes
                else:   
                    self.map[i][ len(self.map[i][j]) - 1 ] = self.border_sprite
                    self.map[i][0] = self.border_sprite

        return self.map

    def set_initial_player_position(self):
        #Posicion inicial del jugador (Coordenadas)
        self.player_position[0] = self.height // 2  
        self.player_position[1] = self.width // 2

        #Dibujamos al jugador en el medio del mapa
        self.map[self.height // 2][self.width // 2] = self.player_sprite

        return self.map

    def player_move(self, entry_move):

        if entry_move == 97:

            #Cambiamos el sprite de donde estaba el jugador
            self.map[self.player_position[0]][self.player_position[1]] = ''
                
            #Renderizamos al jugador en la nueva casilla
            self.map[self.player_position[0]][self.player_position[1] - 1] = self.player_sprite
            self.player_position[0] = self.player_position[0]
            self.player_position[1] = self.player_position[1] - 1
        
        if entry_move == 100:
            self.map[self.player_position[0]][self.player_position[1]] = ''
            self.map[self.player_position[0]][self.player_position[1] + 1] = self.player_sprite
                
            self.player_position[0] = self.player_position[0]
            self.player_position[1] = self.player_position[1] + 1

        if entry_move == 119:
            self.map[self.player_position[0]][self.player_position[1]] = ''
            self.map[self.player_position[0] - 1][self.player_position[1]] = self.player_sprite 

            self.player_position[0] = self.player_position[0] - 1
            self.player_position[1] = self.player_position[1]

        if entry_move == 115:
            self.map[self.player_position[0]][self.player_position[1]] = ''
            self.map[self.player_position[0] + 1][self.player_position[1]] = self.player_sprite

            self.player_position[0] = self.player_position[0] + 1 
            self.player_position[1] = self.player_position[1]


        return self.map

    def render(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print("%3s" %self.map[i][j], end="")
            print()

    def loop(self):

        os.system('cls')

        self.generate_map()    
        self.draw_borders()
        self.set_initial_player_position()

        print("Posicion inicial => ", self.player_position)

        while True:
            self.render()
            
            try:
                self.player_input = input("> ").lower()
                
                if self.player_input == "exit":
                    return

                self.player_move(ord(self.player_input))

            except:
                pass

            print(self.player_position)

            time.sleep(0.5)
            os.system('cls')

    def run(self):
        self.loop()

        print("\n Game over")

if __name__ == "__main__":
    game = Game(30, 20)
    game.run()