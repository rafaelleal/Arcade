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
        self.gold = 0

class Item(arcade.Sprite):
    def __init__(self, image, scale, item_type):
        super().__init__(image, scale)
        self.item_type = item_type  # 'treasure' ou 'trap'

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        # Criar uma instância do personagem
        self.character = Character("character.png", 0.5)
        self.character.center_x = width / 2
        self.character.center_y = height / 2

        # Criar uma lista para armazenar os itens
        self.item_list = arcade.SpriteList()

        # Criar alguns itens e adicioná-los à lista
        for _ in range(10):
            item_type = random.choice(['treasure', 'trap'])
            item_image = "treasure.png" if item_type == 'treasure' else 'trap.png'
            item = Item(item_image, 0.5, item_type)
            item.center_x = random.randint(20, SCREEN_WIDTH - 20)
            item.center_y = random.randint(20, SCREEN_HEIGHT - 20)
            self.item_list.append(item)

    def on_draw(self):
        """ Chamado sempre que precisamos desenhar a janela. """
        arcade.start_render()

        # Desenhar o personagem e os itens
        self.character.draw()
        self.item_list.draw()

        # Desenhar a HUD
        arcade.draw_text(f"HP: {self.character.hp}", 10, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Gold: {self.character.gold}", 10, SCREEN_HEIGHT - 40, arcade.color.BLACK, 14)

    def on_update(self, delta_time):
        """ Chamado a cada frame. """
        self.character.update()

        # Verificar colisões entre o personagem e os itens
        items_hit_list = arcade.check_for_collision_with_list(self.character, self.item_list)
        for item in items_hit_list:
            if item.item_type == 'treasure':
                self.character.gold += 10
            else:  # item_type == 'trap'
                self.character.hp -= 10
            item.remove_from_sprite_lists()  # Remover o item coletado

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