import pygame
import math
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Solar System")

# Function to load images safely
def load_image(filename):
    filepath = os.path.join("C:\\Users\\Kannika M Gowda\\OneDrive\\Desktop\\SolarSystemSimulation\\images", filename)
    return pygame.image.load(filepath).convert_alpha()  # Use convert_alpha for images with transparency

# Load images
sun_img = load_image("sun.png")
mercury_img = load_image("mercury.png")
venus_img = load_image("venus.png")
earth_img = load_image("earth.png")
mars_img = load_image("mars.png")
jupiter_img = load_image("jupiter.png")
saturn_img = load_image("saturn.png")
uranus_img = load_image("uranus.png")
neptune_img = load_image("neptune.png")

# Load and scale background image
background_img = load_image("background.png")
background_img = pygame.transform.scale(background_img, (width, height))

# Scale images to a circular shape
def scale_image(image, size):
    return pygame.transform.scale(image, (size, size))

sun_img = scale_image(sun_img, 120)
mercury_img = scale_image(mercury_img, 30)
venus_img = scale_image(venus_img, 50)
earth_img = scale_image(earth_img, 60)
mars_img = scale_image(mars_img, 50)
jupiter_img = scale_image(jupiter_img, 100)
saturn_img = scale_image(saturn_img, 90)
uranus_img = scale_image(uranus_img, 70)
neptune_img = scale_image(neptune_img, 65)

# Define orbit color
ORBIT_COLOR = (100, 100, 100)  # Gray

# Function to draw a thick elliptical orbit
def draw_ellipse(surface, color, center, width, height, tilt):
    ellipse_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.ellipse(ellipse_surface, color, (0, 0, width, height), 1)  # Thinner ellipse
    ellipse_surface = pygame.transform.rotate(ellipse_surface, tilt)
    surface.blit(ellipse_surface, ellipse_surface.get_rect(center=center))

# Planet class to handle each planet's properties and orbit
class Planet:
    def __init__(self, name, image, distance, speed, orbit_width, orbit_height, tilt, rotation_speed):
        self.name = name
        self.image = image
        self.distance = distance
        self.speed = speed  # Adjust the speed here for each planet
        self.angle = 0
        self.orbit_width = orbit_width
        self.orbit_height = orbit_height
        self.tilt = tilt
        self.rotation_angle = 0
        self.rotation_speed = rotation_speed

    def draw(self, screen, center):
        # Draw thick elliptical orbit
        draw_ellipse(screen, ORBIT_COLOR, center, self.orbit_width, self.orbit_height, self.tilt)

        # Calculate the planet's position in 3D
        x = center[0] + (self.orbit_width // 2) * math.cos(math.radians(self.angle))
        y = center[1] + (self.orbit_height // 2) * math.sin(math.radians(self.angle)) * math.cos(math.radians(self.tilt))
        y -= self.distance * math.sin(math.radians(self.tilt))
        
        # Rotate the planet image
        rotated_image = pygame.transform.rotate(self.image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=(x, y))

        # Draw the planet on the screen
        screen.blit(rotated_image, rotated_rect.topleft)
        
        # Update the angle for the next frame
        if rotate_all or (rotate_single and rotate_single == self):
            self.angle += self.speed
            self.rotation_angle += self.rotation_speed

    def draw_label(self, screen, position, font):
        label = font.render(self.name, True, (255, 255, 255))
        label_rect = label.get_rect(center=(position[0], position[1] + self.image.get_height() // 2 + 20))
        screen.blit(self.image, (position[0] - self.image.get_width() // 2, position[1] - self.image.get_height() // 2))
        screen.blit(label, label_rect)

# Define parameters for each planet
sun = Planet("Sun", sun_img, 0, 0, 0, 0, 0, 0)  # Sun doesn't move
mercury = Planet("Mercury", mercury_img, 50, 1, 200, 100, 7, 1)
venus = Planet("Venus", venus_img, 75, 0.9, 300, 150, 3, 0.5)
earth = Planet("Earth", earth_img, 100, 0.8, 400, 200, 0, 0.3)
mars = Planet("Mars", mars_img, 125, 0.7, 500, 250, 1.85, 0.2)
jupiter = Planet("Jupiter", jupiter_img, 150, 0.6, 600, 300, 1.3, 0.1)
saturn = Planet("Saturn", saturn_img, 175, 0.5, 700, 350, 2.48, 0.05)
uranus = Planet("Uranus", uranus_img, 200, 0.4, 800, 400, 0.77, 0.02)
neptune = Planet("Neptune", neptune_img, 225, 0.3, 900, 450, 1.77, 0.01)

# List of celestial objects
planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Font for labels
font = pygame.font.SysFont("Arial", 24, bold=True)

# Variable to control planet rotation
rotate_all = True
rotate_single = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to close the screen
                running = False
            elif event.key == pygame.K_s:  # Press S to stop rotating
                rotate_all = False
                rotate_single = None
            elif event.key == pygame.K_r:  # Press R to rotate all planets
                rotate_all = True
                rotate_single = None
            elif event.key == pygame.K_1:  # Press 1 for Mercury
                rotate_all = False
                rotate_single = mercury
            elif event.key == pygame.K_2:  # Press 2 for Venus
                rotate_all = False
                rotate_single = venus
            elif event.key == pygame.K_3:  # Press 3 for Earth
                rotate_all = False
                rotate_single = earth
            elif event.key == pygame.K_4:  # Press 4 for Mars
                rotate_all = False
                rotate_single = mars
            elif event.key == pygame.K_5:  # Press 5 for Jupiter
                rotate_all = False
                rotate_single = jupiter
            elif event.key == pygame.K_6:  # Press 6 for Saturn
                rotate_all = False
                rotate_single = saturn
            elif event.key == pygame.K_7:  # Press 7 for Uranus
                rotate_all = False
                rotate_single = uranus
            elif event.key == pygame.K_8:  # Press 8 for Neptune
                rotate_all = False
                rotate_single = neptune

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw the planets and orbits
    for planet in planets:
        planet.draw(screen, (width // 2, height // 2))

    # Draw the planets and labels at the bottom
    bottom_margin = 100
    gap = (width - 9 * 80) // 10  # 9 planets, 80px each, plus gaps
    x_position = gap
    for planet in planets:
        planet.draw_label(screen, (x_position, height - bottom_margin), font)
        x_position += 80 + gap

    pygame.display.flip()

pygame.quit()
