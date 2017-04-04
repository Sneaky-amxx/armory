import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class GetObjectNode(Node, ArmLogicTreeNode):
    '''Get object node'''
    bl_idname = 'LNGetObjectNode'
    bl_label = 'Get Object'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketString', "Name")
        self.outputs.new('NodeSocketShader', "Object")

add_node(GetObjectNode, category='Value')
