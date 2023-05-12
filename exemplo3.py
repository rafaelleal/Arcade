import arcade

# Definir constantes para a largura e altura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Character(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        # Criar uma instância do personagem
        self.character = Character("character.png", 0.5)
        self.character.center_x = width / 2
        self.character.center_y = height / 2

    def on_draw(self):
        """ Chamado sempre que precisamos desenhar a janela. """
        arcade.start_render()

        # Desenhar o personagem
        self.character.draw()

    def on_update(self, delta_time):
        """ Chamado a cada frame. """
        self.character.update()

    def on_key_press(self, key, modifiers):
        """ Chamado sempre que uma tecla é pressionada. """
        if key == arcade.key.UP:
            self.character.change_y = self.character.speed
        elif key == arcade.key.DOWN:
            self.character.change_y = -self.character.speed
        elif key == arcade.key.LEFT:
            self.character.change_x = -self.character.speed
        elif key == arcade.key.RIGHT:
            self.character.change_x = self.character.speed

    def on_key_release(self, key, modifiers):
        """ Chamado quando o usuário solta uma tecla. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.character.change_x = 0

def main():
    """ Função principal """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
