# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *
from light import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("FPSScene")
    scene.camera = Camera(False, res_x, res_y)

    # creates a light
    scene.light = Light("sun")
    scene.light.position= vector3(1,5,1)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    obj6 = Object3d("TestObjectpol")
    obj6.scale = vector3(0.5, 0.5, 0.5)
    obj6.position = vector3(1, -0.3, -0.5)
    obj6.mesh = Mesh.create_pol((2,1,2))
    obj6.material = Material(color(1,0,0.60,1), "TestMaterial1")
    scene.add_object(obj6)

    obj5 = Object3d("TestObjectpyramid")
    obj5.scale = vector3(0.5, 0.5, 1)
    obj5.position = vector3(2, 2, 3)
    obj5.mesh = Mesh.create_pyramid((1,2,1))
    obj5.material = Material(color(0,1,1,1), "TestMaterial1")
    scene.add_object(obj5)

    obj4 = Object3d("TestObjectcube2")
    obj4.scale = vector3(0.5, 0.5, 1)
    obj4.position = vector3(-1, 0, 1)
    obj4.mesh = Mesh.create_cube((1,1,1))
    obj4.material = Material(color(1,1,1,1), "TestMaterial1")
    scene.add_object(obj4)

    obj3 = Object3d("TestObjectcube")
    obj3.scale = vector3(0.5, 0.5, 1)
    obj3.position = vector3(1, 0, 0.5)
    obj3.mesh = Mesh.create_cube((1,1,1))
    obj3.material = Material(color(1,0,1,1), "TestMaterial1")
    scene.add_object(obj3)

    # Create a reed polygon
    obj2 = Object3d("TestObjectpol")
    obj2.scale = vector3(0.5, 0.5, 0.5)
    obj2.position = vector3(0, 0, 1.5)
    obj2.mesh = Mesh.create_pol((1,1,1))
    obj2.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj2)

    # Create a green pyremid as a 
    obj1 = Object3d("testObjectplayer")
    obj1.position += vector3(0, 0.75, 0)
    obj1.mesh = Mesh.create_pyramid((0.5, 0.5, 1))
    obj1.material = Material(color(0,0.75,0,1), "TestMaterial2")
    scene.add_object(obj1)

    # Specify the rotation of the object. It will rotate when the arrow keys are pressed down
    angle = 15
    axisY = vector3(0,1,0)
    axisY.normalize()
    axisX = vector3(1,0,0)
    axisX.normalize()
    axisZ = vector3(0,0,1)
    axisZ.normalize()

    mov = 0.2

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                #rotação
                elif (event.key == pygame.K_LEFT):
                    q = from_rotation_vector((axisY * math.radians(-(angle))).to_np3())
                    obj1.rotation = q * obj1.rotation
                elif (event.key == pygame.K_RIGHT):
                    q = from_rotation_vector((axisY * math.radians(angle)).to_np3())
                    obj1.rotation = q * obj1.rotation
                elif (event.key == pygame.K_DOWN):
                    q = from_rotation_vector((axisX * math.radians(angle)).to_np3())
                    obj1.rotation = q * obj1.rotation
                elif (event.key == pygame.K_UP):
                    q = from_rotation_vector((axisX * math.radians(-(angle))).to_np3())
                    obj1.rotation = q * obj1.rotation
                elif (event.key == pygame.K_KP_PLUS):
                    q = from_rotation_vector((axisZ * math.radians(-(angle))).to_np3())
                    obj1.rotation = q * obj1.rotation
                elif (event.key == pygame.K_KP_MINUS):
                    q = from_rotation_vector((axisZ * math.radians(angle)).to_np3())
                    obj1.rotation = q * obj1.rotation
                #posicão
                elif (event.key == pygame.K_LSHIFT):
                    obj1.position += vector3(0, -mov, 0)
                elif (event.key == pygame.K_SPACE):
                    obj1.position += vector3(0, mov, 0)
                elif (event.key == pygame.K_a):
                    obj1.position += vector3(-mov, 0, 0)
                elif (event.key == pygame.K_d):
                    obj1.position += vector3(mov, 0, 0)
                elif (event.key == pygame.K_s):
                    obj1.position += vector3( 0, 0, -mov)
                elif (event.key == pygame.K_w):
                    obj1.position += vector3( 0, 0, mov)
                elif (event.key == pygame.K_t):
                    for i in obj1.mesh.origins:
                        print(i)
                        print(obj1.position.z + i.z)
                        print(scene.camera.position.z)
                        print("/")

        scene.camera.position = obj1.position - vector3(0,-0.5,2.5)


        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
