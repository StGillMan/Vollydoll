import maya.cmds as cmds

def checkInputPoly(input=None):
    if input:
        if isinstance(input, list):
            notPolyObj = [x for x in input if not cmds.filterExpand(x, sm=12)]
            if notPolyObj:
                return False
            else:
                return True 
                    



