import arcade
import random

# Definir constantes para a largura e altura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Character(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 5
        self.hp = 100

class Enemy(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 2
        self.hp = 50
        self.change_direction_counter = 0

    def update(self):
        if self.change_direction_counter <= 0:
            # Muda a direção aleatoriamente
            self.change_x = random.choice([-self.speed, 0, self.speed])
            self.change_y = random.choice([-self.speed, 0, self.speed])
            self.change_direction_counter = 60  # Muda a direção a cada 60 frames
        else:
            self.change_direction_counter -= 1

        # Movimenta o inimigo
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Mantém o inimigo dentro da tela
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        # Criar uma instância do personagem
        self.character = Character("character.png", 0.5)
        self.character.center_x = width / 2
        self.character.center_y = height / 2

        # Criar uma instância do inimigo
        self.enemy = Enemy("enemy.png", 0.5)
        self.enemy.center_x = random.randint(0, SCREEN_WIDTH)
        self.enemy.center_y = random.randint(0, SCREEN_HEIGHT)

    def on_draw(self):
        """ Chamado sempre que precisamos desenhar a janela. """
        arcade.start_render()

        # Desenhar o personagem e o inimigo
        self.character.draw()
        self.enemy.draw()

        # Desenhar a HUD
        arcade.draw_text(f"Player HP: {self.character.hp:.0f}", 10, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Enemy HP: {self.enemy.hp}", 10, SCREEN_HEIGHT - 40, arcade.color.BLACK, 14)

    def on_update(self, delta_time):
        """ Chamado a cada frame. """
        self.character.update()
        self.enemy.update()

        # Verificar colisões entre o personagem e o inimigo
        if arcade.check_for_collision(self.character, self.enemy):
            self.character.hp -= 1
            self.enemy.hp -= 1
            self.in_combat = True

            if self.enemy.hp <= 0:
                self.enemy.kill()
                self.enemy = Enemy("enemy.png", 0.5)
                self.enemy.center_x = random.randint(0, SCREEN_WIDTH)
                self.enemy.center_y = random.randint(0, SCREEN_HEIGHT)
        else:
            self.in_combat = False

        # Regenerar HP fora do combate
        if not self.in_combat and self.character.hp < 100:
            self.character.hp += 0.01  # Regenerar 0.1 HP por frame


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

