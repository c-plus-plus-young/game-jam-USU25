import pygame
import random

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, backgroundWidth, backgroundHeight):
        super().__init__()
        self.type = "obs"

        # Load and scale obstacle image
        self.image = pygame.image.load('images/obs.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.width, self.height = self.image.get_size()

        # Set initial position of the obstacle, ensuring it stays within the bounds
        self.x = random.randint(0, backgroundWidth - self.width)
        self.y = random.randint(0, backgroundHeight - self.height)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def getPosition(self):
        """Return the current position of the obstacle."""
        return self.x, self.y

    def update(self):
        """Update logic for obstacles (if needed)."""
        pass

    @classmethod
    def reset_obstacles(cls, backgroundWidth, backgroundHeight, count):
        """
        Delete all current obstacles and recreate them.
        :param backgroundWidth: Width of the background area
        :param backgroundHeight: Height of the background area
        :param count: Number of obstacles to recreate
        """
        # Clear the existing obstacle group
        cls.all_obstacles.empty()

        # Recreate the obstacles
        for _ in range(count):
            Obstacle(backgroundWidth, backgroundHeight)