from arm.logicnode.arm_nodes import *

class GetFPSNode(ArmLogicTreeNode):
    """Get the frames per second count."""
    bl_idname = 'LNGetFPSNode'
    bl_label = 'Get Frames Per Second'
    arm_version = 1

    def init(self, context):
        super(GetFPSNode, self).init(context)
        self.add_output('ArmIntSocket', 'Count')
