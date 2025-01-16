import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar dan judul
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Ular")

# Warna-warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Fungsi untuk menggambar ular
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Fungsi untuk menampilkan pesan
def message(msg, color):
    font_style = pygame.font.SysFont(None, 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/6, height/3])

# Loop utama permainan
def game_loop():
    game_over = False
    game_close = False

    # Posisi awal ular dan makanan
    x1 = width/2
    y1 = height/2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, height - 10) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(white)
            message("Kamu Kalah! Q-Quit/C-Play Lagi", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        # Batas layar
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update posisi ular
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)

        # Gambar makanan
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])

        # Tambahkan kepala ular ke list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        # Hapus ekor jika ular bertambah panjang
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Cek tabrakan dengan tubuh sendiri
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        # Gambar ular
        draw_snake(10, snake_list)

        # Perbarui tampilan
        pygame.display.update()

        # Jika ular memakan makanan
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, height - 10) / 10.0) * 10.0
            length_of_snake += 1

        # Atur kecepatan permainan
        pygame.time.Clock().tick(15)

    pygame.quit()
    quit()

game_loop()