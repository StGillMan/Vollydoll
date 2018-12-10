import maya.cmds as cmds
cmds.setAttr
def checkFaces(obj=None):
    returnDict = {}
    if obj:
        if isinstance(obj, list):
            
            for object in obj:
                if cmds.filterExpand(object, sm=12):
                    faceFix = []
                    allFaces = cmds.polyListComponentConversion(object, tf=True)
                    faceList = cmds.ls(allFaces, fl=True)
                    for face in faceList:
                        vertex = cmds.polyListComponentConversion(face, tv=True)
                        countVertex = len(cmds.ls(vertex, fl=True))
                        if not countVertex == 4:
                            faceFix.append(face)
                    
                    returnDict[object] = faceFix
            
            selectFaces = [x for key, value in returnDict.iteritems() for x in value]
            cmds.select(selectFaces)
            
            return returnDict



