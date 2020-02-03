from camera import *
from operator import itemgetter


class Scene:
    def __init__(self, name):
        self.name = name
        self.camera = Camera(True, 640, 480)
        self.objects = []
        self.light = None

    def add_object(self, obj):
        self.objects.append(obj)
        self.sort()


    def render(self, screen):
        camera_matrix = self.camera.get_camera_matrix()
        projection_matrix = self.camera.get_projection_matrix()
        self.sort()

        clip_matrix = camera_matrix @ projection_matrix

        for obj in self.objects:
            obj.render( screen, clip_matrix, self.camera.position, self.light.position)

    def sort(self):
        self.objects.sort(key=lambda Object3d: Object3d.position.z, reverse=True)

