import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Label changeant de couleur de manière fluide")

# Définir les couleurs
WHITE = (255, 255, 255)

# Créer une horloge pour contrôler le framerate
clock = pygame.time.Clock()

# Initialiser une police pour afficher le texte
font = pygame.font.SysFont(None, 36)

# Fonction pour interpoler entre deux couleurs
def lerp_color(color1, color2, t):
    return (
        color1[0] + (color2[0] - color1[0]) * t,
        color1[1] + (color2[1] - color1[1]) * t,
        color1[2] + (color2[2] - color1[2]) * t
    )

# Fonction principale du jeu
def main():
    color1 = (255, 0, 0)
    color2 = (0, 0, 255)
    t = 0
    direction = 1
    speed = 0.01  # Vitesse de changement de couleur

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mettre à jour la valeur de t
        t += direction * speed
        if t >= 1 or t <= 0:
            direction *= -1
            t = max(0, min(1, t))  # Assurer que t reste dans les limites [0, 1]

        # Calculer la couleur actuelle en interpolant entre color1 et color2
        current_color = lerp_color(color1, color2, t)

        # Remplir l'écran avec une couleur
        screen.fill(WHITE)

        # Rendre le texte avec la couleur actuelle
        label_text = font.render("Label qui change de couleur", True, current_color)

        # Afficher le texte sur l'écran
        screen.blit(label_text, (10, 10))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le framerate à 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
