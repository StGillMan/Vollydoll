import maya.cmds as cmds


def copyVertexNm(input_vtx=None):
    """
    This function copy pervertex normal
    and it can be pasted on other selected
    vertex, or on same loop or exactly the
    same object
    :param input_vtx:
    :return:
    """
    if not input_vtx:
        input_vtx = cmds.ls(sl=True)[0]
    if input_vtx:
        if isinstance(input_vtx, list):
            cmds.select(input_vtx[0])
        elif isinstance(input_vtx, basestring):
            cmds.select(input_vtx)

        try:
            vertexNm = cmds.polyNormalPerVertex(query=True, xyz=True)
        except:
            print 'You have no select'

        if vertexNm:
            return vertexNm
        else:
            return []


vertexNm = copyVertexNm()