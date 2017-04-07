import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class RemoveObjectNode(Node, ArmLogicTreeNode):
    '''Remove object node'''
    bl_idname = 'LNRemoveObjectNode'
    bl_label = 'Remove Object'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketOperator', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.outputs.new('ArmNodeSocketOperator', 'Out')

add_node(RemoveObjectNode, category='Operator')
