import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load hình ảnh nhân vật
        self.image = pygame.image.load("assets/player.png").convert_alpha()  # Thay "assets/player.png" bằng đường dẫn tới ảnh
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100
        self.speed = 5
        self.weapon = "sung_thuong"  # Khởi tạo vũ khí

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def take_damage(self, damage):
        self.health -= damage

    def shoot(self):
        # Tạo đối tượng Bullet và thêm vào group bullet
        pass  # Cần hoàn thiện sau

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):  # direction là vector chỉ hướng bay
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()  # Thay "assets/bullet.png" bằng đường dẫn
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.direction = direction

    def update(self):
        # Di chuyển viên đạn theo hướng direction
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        
