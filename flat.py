import maya.cmds as cmds

def flattenList(list=None):
    flattenList = []
    
    if list:
        for l in list:
            listFlat = cmds.ls(l, fl=True)
            for each in listFlat:
                flattenList.append(each)
    
    return flattenList
