from arm.logicnode.arm_nodes import *

class BooleanArrayNode(ArmLogicTreeNode):
    """Stores an array of boolean elements as a variable."""
    bl_idname = 'LNArrayBooleanNode'
    bl_label = 'Array Boolean'
    arm_version = 1
    arm_section = 'variable'

    def __init__(self):
        super(BooleanArrayNode, self).__init__()
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(BooleanArrayNode, self).init(context)
        self.add_output('ArmNodeSocketArray', 'Array', is_var=True)
        self.add_output('NodeSocketInt', 'Length')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketBool'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))

    def draw_label(self) -> str:
        if len(self.inputs) == 0:
            return self.bl_label

        return f'{self.bl_label}: [{len(self.inputs)}]'
