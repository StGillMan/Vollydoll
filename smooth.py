import maya.cmds as cmds
import inPoly

def getSmooth(obj=None, fix=True):
    """
    This function check input
    and return true if smooth mode is 3 and 2,
    or false if it's 1
    :param obj: 'list'
    :param fix: 'bool'
    :return: 'dict'
    """
    returnDict = {}
    if obj:
        for o in obj:
            if inPoly.checkInputPoly([o]):
                smooth = cmds.displaySmoothness(o, q=True, po=True)
                if smooth:
                    returnDict[o] = smooth
                    if fix:
                        if smooth == [2L] or [3L]:
                            cmds.displaySmoothness(o, po=1)
    return returnDict

