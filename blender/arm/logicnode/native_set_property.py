import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SetPropertyNode(Node, ArmLogicTreeNode):
    '''Set property node'''
    bl_idname = 'LNSetPropertyNode'
    bl_label = 'Set Property'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', "In")
        self.inputs.new('NodeSocketShader', "Object")
        self.inputs.new('NodeSocketString', "Property")
        self.inputs.new('NodeSocketShader', "Value")
        self.outputs.new('NodeSocketShader', "Out")

add_node(SetPropertyNode, category='Native')
