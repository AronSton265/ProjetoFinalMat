import pygame
import numpy as np
from vector3 import *
from quaternion import *
import math

class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []
        self.origins = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material, obj, camarapos):
        c = material.color.tuple3()        
        i=-1
        for poly in self.polygons:
            i=i+1
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            ab=(poly[1].to_np4() @ obj.get_matrix())-(poly[0].to_np4() @ obj.get_matrix())
            abvec=vector3(0,0,0)
            abvec.x=ab[0]
            abvec.y=ab[1]
            abvec.z=ab[2]
            bc=(poly[2].to_np4() @ obj.get_matrix())-(poly[1].to_np4() @ obj.get_matrix())
            bcvec=vector3(0,0,0)
            bcvec.x=bc[0]
            bcvec.y=bc[1]
            bcvec.z=bc[2]
            n = vector3.cross(abvec, bcvec)
            np.cross
            centro = self.origins[i].to_np4()
            centro = centro @ obj.get_matrix()
            v=centro-camarapos.to_np4()
            normal=n.to_np4()
            

            if(np.dot( v, normal) < 0.0):
                pygame.draw.polygon(screen, c, tpoly, material.line_width)


    @staticmethod
    def create_cube(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownCube")

        #quadrados esquerda e direita
        Mesh.create_quad(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)

        #quadrados baixo e cima
        Mesh.create_quad(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)

        #quadrados frente e traz
        Mesh.create_quad(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0,0,0), mesh)

        return mesh

    @staticmethod
    def create_quad(origin, axis0, axis1, axis2, mesh):
        if (mesh == None):
            mesh = Mesh("UnknownQuad")

        #vertices
        poly = []
        poly.append(origin + axis0 + axis1)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1 + axis2)
        poly.append(origin - axis0 + axis1 + axis2)

        mesh.polygons.append(poly)
        mesh.origins.append(origin)

        return mesh
    
    @staticmethod
    def create_pyramid(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownPyramid")

        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)

        #traz/frente
        Mesh.create_tria(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0, 0, -size[2] * 0.5), mesh)
        Mesh.create_tria(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        #direita/esquerda
        Mesh.create_tria(vector3( size[0] * 0.5, 0, 0), vector3( 0, 0,  size[2] * 0.5), vector3(0, size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0, 0), mesh)
        Mesh.create_tria(vector3(-size[0] * 0.5, 0, 0), vector3( 0, 0, -size[2] * 0.5), vector3(0, size[1] * 0.5, 0), vector3( size[0] * 0.5, 0, 0), mesh)
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
        mesh.origins.append(origin)

        return mesh

    
    @staticmethod
    def create_pol(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownPol")

        #quadrados direita
        Mesh.create_quad(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.25, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3( size[0] * 0.25, size[1] * 0.40, 0), vector3(0, size[1] * 0.125, 0), vector3(0, 0, -size[2] * 0.5), vector3(size[0] * 0.25,0,0), mesh)
        Mesh.create_quad(vector3( size[0] * 0.5, -size[1] * 0.40, 0),vector3(0, size[1] * 0.125, 0), vector3(0, 0, -size[2] * 0.5), vector3(-size[0] * 0.25,0,0), mesh)

        #quadrados esquerda
        Mesh.create_quad(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.25, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3(-size[0] * 0.25, size[1] * 0.40, 0), vector3(0, size[1] * 0.125, 0), vector3(0, 0, size[2] * 0.5), vector3(-size[0] * 0.25,0,0),mesh)
        Mesh.create_quad(vector3(-size[0] * 0.5, -size[1] * 0.40, 0), vector3(0, size[1] * 0.125, 0), vector3(0, 0, size[2] * 0.5), vector3(size[0] * 0.25,0,0),mesh)

        #quadrados baixo e cima
        Mesh.create_quad(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.25, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)
        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.25, 0), vector3(0, 0, size[2] * 0.5), vector3(0,0,0), mesh)

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
        mesh.origins.append(origin)

        return mesh
