import maya.cmds as cmds

def checkStars(obj=None):
    returnDict = {}
    
    if obj:
        if checkInputPoly(obj):
            for object in obj:
                selectEdge = []
                allVertex = cmds.polyListComponentConversion(object, tv=True)
                flatVertex = flattenList(allVertex)
                for vertex in flatVertex:
                    edgeOnVertex = cmds.polyListComponentConversion(vertex, te=True)
                    flatEdge = flattenList(edgeOnVertex)
                    if len(flatEdge) > 5:
                        for edge in flatEdge:
                            selectEdge.append(edge)
                
                returnDict[object] = selectEdge

    selectEdge = [x for key, value in returnDict.iteritems() for x in value]
    cmds.select(selectEdge)
    
    return returnDict

