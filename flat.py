import maya.cmds as cmds


def flattenList(obj=None):
    """Decomposes the components

    :param obj: 'list' objects or components
    :return: 'list' list of decomposes items
    """
    flattenList = []

    if obj:
        for l in obj:
            listFlat = cmds.ls(l, fl=True)
            for item in listFlat:
                flattenList.append(item)

    return flattenList
