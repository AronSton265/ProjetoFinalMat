import pygame
from vector3 import *
import math

class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material):
        c = material.color.tuple3()        

        for poly in self.polygons:
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            pygame.draw.polygon(screen, c, tpoly, material.line_width)


    @staticmethod
    def create_cube(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownCube")

        #quadrados esquerda e direita
        Mesh.create_quad(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        #quadrados baixo e cima
        Mesh.create_quad(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        #quadrados frente e traz
        Mesh.create_quad(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_quad(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)

        return mesh

    @staticmethod
    def create_quad(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("UnknownQuad")

        #vertices
        poly = []
        poly.append(origin + axis0 + axis1)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1)
        poly.append(origin - axis0 + axis1)

        mesh.polygons.append(poly)

        return mesh

    @staticmethod
    def create_pyramid(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownPyramid")

        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        Mesh.create_tria(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0, 0, -size[2] * 0.5), mesh)
        Mesh.create_tria(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        return mesh

    @staticmethod
    def create_tria(origin, axis0, axis1, axis2, mesh):
        if (mesh == None):
            mesh = Mesh("UnknownTria")

        poly = []
        poly.append(origin + axis1 + axis2)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1)

        mesh.polygons.append(poly)

        return mesh
    
    @staticmethod
    def create_pol(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownPol")

        #quadrados esquerda e direita
        Mesh.create_quad(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.25, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.25, 0), vector3(0, 0, size[2] * 0.5), mesh)

        #quadrados baixo e cima
        Mesh.create_quad(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.25, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.25, 0), vector3(0, 0, size[2] * 0.5), mesh)

        #quadrados frente e traz
        Mesh.create_hex(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_hex(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)

        return mesh

    @staticmethod
    def create_hex(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("UnknownHex")

        #vertices
        poly = []
        poly.append(origin + axis0/2 + axis1)
        poly.append(origin + axis0 + axis1/2)
        poly.append(origin + axis0 - axis1/2)
        poly.append(origin + axis0/2 - axis1)
        poly.append(origin - axis0/2 - axis1)
        poly.append(origin - axis0 - axis1/2)
        poly.append(origin - axis0 + axis1/2)
        poly.append(origin - axis0/2 + axis1)
        

        mesh.polygons.append(poly)

        return mesh
