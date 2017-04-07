import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SetVariableNode(Node, ArmLogicTreeNode):
    '''SetVariable node'''
    bl_idname = 'LNSetVariableNode'
    bl_label = 'Set Variable'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketOperator', 'In')
        self.inputs.new('NodeSocketShader', 'Variable')
        self.inputs.new('NodeSocketShader', 'Value')
        self.outputs.new('ArmNodeSocketOperator', 'Out')

add_node(SetVariableNode, category='Operator')
