import arcade

# Definir constantes para a largura e altura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Character(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        # Criar uma instância do personagem
        self.character = Character("character.png", 1.0)
        self.character.center_x = width / 2
        self.character.center_y = height / 2

    def on_draw(self):
        """ Chamado sempre que precisamos desenhar a janela. """
        arcade.start_render()

        # Desenhar o personagem
        self.character.draw()

def main():
    """ Função principal """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
