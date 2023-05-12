import arcade

# Definir constantes para a largura e altura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Chamado sempre que precisamos desenhar a janela. """
        arcade.start_render()

def main():
    """ Função principal """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
