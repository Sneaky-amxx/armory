import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class PrintNode(Node, ArmLogicTreeNode):
    '''Print node'''
    bl_idname = 'LNPrintNode'
    bl_label = 'Print'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', "In")
        self.inputs.new('NodeSocketShader', "Value")
        self.outputs.new('NodeSocketShader', "Out")

add_node(PrintNode, category='Operator')
