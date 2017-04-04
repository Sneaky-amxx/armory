import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class GetVisibleNode(Node, ArmLogicTreeNode):
    '''Get visible node'''
    bl_idname = 'LNGetVisibleNode'
    bl_label = 'Get Visible'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', "Object")
        self.outputs.new('NodeSocketBool', "Visible")

add_node(GetVisibleNode, category='Value')
