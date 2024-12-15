import turtle
import math
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Solar System Visualization")

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)  # Adjust the size of the sun

# Function to create a planet
def create_planet(color, radius, speed):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.penup()
    planet.speed(0)
    planet.orbit_radius = radius
    planet.orbit_speed = speed
    planet.angle = 0
    return planet

# Create planets
mercury = create_planet("gray", 50, 4)
venus = create_planet("orange", 80, 3)
earth = create_planet("blue", 120, 2)
mars = create_planet("red", 160, 1.5)
jupiter = create_planet("brown", 200, 1)
saturn = create_planet("gold", 250, 0.8)
uranus = create_planet("light blue", 300, 0.5)
neptune = create_planet("dark blue", 350, 0.3)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Function to draw the orbits
def draw_orbits():
    orbit_drawer = turtle.Turtle()
    orbit_drawer.hideturtle()
    orbit_drawer.speed(0)
    orbit_drawer.color("black")
    orbit_drawer.penup()
    for planet in planets:
        orbit_drawer.goto(0, -planet.orbit_radius)
        orbit_drawer.pendown()
        orbit_drawer.circle(planet.orbit_radius)
        orbit_drawer.penup()

draw_orbits()

# Move the planets in their orbits
while True:
    for planet in planets:
        # Calculate the x and y positions
        planet.angle += planet.orbit_speed
        x = planet.orbit_radius * math.cos(math.radians(planet.angle))
        y = planet.orbit_radius * math.sin(math.radians(planet.angle))
        planet.goto(x, y)

    time.sleep(0.01)  # Delay to control animation speed
