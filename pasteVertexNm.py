import maya.cmds as cmds
select = cmds.ls(sl = True)

def pasteVertexNm (input=select, vertexNm = vertexNm ):
      """
    This function paste perVertex normal
    :param obj: 'list' vertex
    :return: 'list' pacted pervertex normal
    """
       if input:
        if isinstance(input, list):
            pastedNm = cmds.polyNormalPerVertex( x = (vertexNm[0]), y=(vertexNm[1]), z=(vertexNm[2]))
            return  pastedNm
                
            
pasteVertexNm()
