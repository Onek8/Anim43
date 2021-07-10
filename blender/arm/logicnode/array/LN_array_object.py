from arm.logicnode.arm_nodes import *

class ObjectArrayNode(ArmLogicTreeNode):
    """Stores an array of object elements as a variable."""
    bl_idname = 'LNArrayObjectNode'
    bl_label = 'Array Object'
    arm_version = 1
    arm_section = 'variable'

    def __init__(self):
        super(ObjectArrayNode, self).__init__()
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(ObjectArrayNode, self).init(context)
        self.add_output('ArmNodeSocketArray', 'Array', is_var=True)
        self.add_output('ArmIntSocket', 'Length')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'ArmNodeSocketObject'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))

    def draw_label(self) -> str:
        if len(self.inputs) == 0:
            return self.bl_label

        return f'{self.bl_label}: [{len(self.inputs)}]'
