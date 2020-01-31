# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

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
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Specify the rotation of the object. It will rotate when the arrow keys are pressed down
    angle = 15
    axisY = vector3(0,1,0)
    axisY.normalize()
    axisX = vector3(1,0,0)
    axisX.normalize()
    axisZ = vector3(0,0,1)
    axisZ.normalize()

    mov = 0.2

    # Timer
    #delta_time = 0
    #prev_time = time.time()

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
                elif (event.key == pygame.K_s):
                    obj1.position += vector3(0, -mov, 0)
                elif (event.key == pygame.K_w):
                    obj1.position += vector3(0, mov, 0)
                elif (event.key == pygame.K_a):
                    obj1.position += vector3(-mov, 0, 0)
                elif (event.key == pygame.K_d):
                    obj1.position += vector3(mov, 0, 0)
                elif (event.key == pygame.K_q):
                    obj1.position += vector3( 0, 0, -mov)
                elif (event.key == pygame.K_e):
                    obj1.position += vector3( 0, 0, mov)

#como o meu comutador nao tem as teclas pgup e pgdown para o trabalho as mesmas serao trocadas por + e - respetivamente do key pad


        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        #delta_time = time.time() - prev_time
        #prev_time = time.time()


# Run the main function
main()
