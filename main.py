import pygame
import sys
from krople import Krople

class KropleDeszczu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.image = pygame.image.load('pictures/las.bmp')
        self.screen_rect = self.image.get_rect()
        #self.bg_color = (160, 160, 160)
        pygame.display.set_caption('Krople Deszczu')
        self.krople = pygame.sprite.Group()
        self.create_krople()

    def run_animation(self):
        while True:
            self.key_down_event()
            self._update_krople()
            self.run_screen()


    def key_down_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def create_krople(self):
        kropla = Krople(self)
        kropla_width, krople_height = kropla.rect.size
        avaible_space = self.screen_rect.width - (2 * kropla_width)
        number_krople = avaible_space // (2 * kropla_width)

        for kropla_number in range(number_krople):
            kropla = Krople(self)
            kropla.x = kropla_width + (2 * kropla_width * kropla_number)
            kropla.rect.x = kropla.x
            self.krople.add(kropla)

    def run_screen(self):
        self.screen.blit(self.image, self.screen_rect)
        self.krople.draw(self.screen)
        pygame.display.flip()

    def _update_krople(self):
        self.krople.update()
        make_new_drops = False
        for kropla in self.krople.copy():
            if kropla.check_bottom_edge():
                self.krople.remove(kropla)
                make_new_drops = True
        if make_new_drops:
            self.create_krople()

if __name__ == '__main__':
    ai_animation = KropleDeszczu()
    ai_animation.run_animation()