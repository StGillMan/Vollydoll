import maya.cmds as cmds
import inPoly
import flat
def checkStars(obj=None):
    """
        This function check inputs
        adn return dict of object name
        and list of his not relevant edges
        :param obj: 'list' poly objects
        :return: 'dict'
        """
    returnDict = {}
    
    if obj:
        if inPoly.checkInputPoly(obj):
            for object in obj:
                selectEdge = []
                allVertex = cmds.polyListComponentConversion(object, tv=True)
                flatVertex = flat.flattenList(allVertex)
                for vertex in flatVertex:
                    edgeOnVertex = cmds.polyListComponentConversion(vertex, te=True)
                    flatEdge = flat.flattenList(edgeOnVertex)
                    if len(flatEdge) > 5:
                        for edge in flatEdge:
                            selectEdge.append(edge)
                
                returnDict[object] = selectEdge

    selectEdge = [x for key, value in returnDict.iteritems() for x in value]
    cmds.select(selectEdge)
    
    return returnDict

