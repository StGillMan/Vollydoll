import maya.cmds as cmds

def flattenList(list=None):
    """
    This function processes the input list
    and returns the expanded list of objects.
    :param list: 'list' anything selected objects
    :return: 'list'
    """
    flattenList = []
    
    if list:
        for l in list:
            listFlat = cmds.ls(l, fl=True)
            for each in listFlat:
                flattenList.append(each)
    
    return flattenList

