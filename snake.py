import pygame
import sys
import random

# Oyun tahtası boyutları
WIDTH, HEIGHT = 400, 400

# Renkler
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Yılanın hızı ve başlangıç boyutu
SNAKE_SPEED = 10  # Yılan hızı
SNAKE_SIZE = 20

# Skor
score = 0
high_score = 0

# En yüksek skoru bir dosyadan okuma
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    # Dosya yoksa veya skor kaydedilmemişse varsayılan en yüksek skor 0 olarak kalır
    pass

# Ekran oluşturma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

# Yılanın başlangıç pozisyonu ve hızı
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed_x = 0
snake_speed_y = 0

# Yılanın vücut parçaları
snake_body = []
snake_length = 1

# Yem başlangıç pozisyonu
food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

# Oyun döngüsü
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # En yüksek skoru dosyaya yazma
            with open("highscore.txt", "w") as file:
                file.write(str(high_score))
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed_x = 0
                snake_speed_y = -SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_speed_x = 0
                snake_speed_y = SNAKE_SIZE
            if event.key == pygame.K_LEFT:
                snake_speed_x = -SNAKE_SIZE
                snake_speed_y = 0
            if event.key == pygame.K_RIGHT:
                snake_speed_x = SNAKE_SIZE
                snake_speed_y = 0

    # Yılanın yeni pozisyonunu hesaplama
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # Yılanın tahtadan çıkmasını engelleme
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        font = pygame.font.Font(None, 36)
        text = font.render(f"DEAD - Skor: {score} - En Yüksek Skor: {high_score} (Yeniden başlamak için bir tuşa basın)", True, GREEN)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(1000)  # 1 saniye bekle

        # Oyuncu herhangi bir tuşa basana kadar bekleyin
        waiting_for_keypress = True
        while waiting_for_keypress:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting_for_keypress = False
                    # Yılanın başlangıç pozisyonunu yeniden ayarlayın
                    snake_x = WIDTH // 2
                    snake_y = HEIGHT // 2
                    snake_speed_x = 0
                    snake_speed_y = 0
                    snake_body = []
                    snake_length = 1
                    score = 0
                    game_over = False
                    # Yemi yeni bir konuma yerleştirin
                    food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
                    food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
                    screen.fill(BLACK)  # Ekranı temizle
                    pygame.display.update()

    # ... Diğer kodlar ...

    # Yılanın yemi yemesi
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        score += 10  # Yem yendiğinde skoru 10 artır

        if score > high_score:
            high_score = score  # En yüksek skoru güncelle

        # Yeni bir yem konumu ayarlama
        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

    # ... Diğer kodlar ...

    # Skoru ekrana yazdırma
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Skor: {score}", True, GREEN)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)  # Skoru sol üst köşeye yerleştir
    screen.blit(score_text, score_rect)

    high_score_text = font.render(f"En Yüksek Skor: {high_score}", True, GREEN)
    high_score_rect = high_score_text.get_rect()
    high_score_rect.topleft = (10, 50)  # En yüksek skoru biraz aşağıya yerleştir
    screen.blit(high_score_text, high_score_rect)

    # ... Diğer kodlar ...

# ... Diğer kodlar ...
