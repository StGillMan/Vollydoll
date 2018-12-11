import maya.cmds as cmds
import inPoly

def visibility(obj=None, fix=True):
    """
    This functioncheck input
    and return dict of object
    and his primary visibility
    Also it's chenge primary visibility to 1
    I don't know how to get dict of shape node render stats attr
    :param obj: 'list'
    :param fix: 'bool'
    :return: 'dict'
    """
    returnDict = {}
    if obj:
        for o in obj:
            if inPoly.checkInputPoly([o]):
                if o.primaryVisibility == 0:
                    prVis = cmds.setAttr('o.prumaryVisibility', 1)

