import maya.cmds as cmds

def checkInputPoly(input=None):
    """
    This function check inputs and
    return true if it polygonal mesh,
    or false if isn't
    :param input: 'list'
    :return: 'bool'
    """
    if input:
        if isinstance(input, list):
            notPolyObj = [x for x in input if not cmds.filterExpand(x, sm=12)]
            if notPolyObj:
                return False
            else:
                return True 
                    



