import maya.cmds as cmds

selece = cmds.ls(sl=True)
def setNm(input_obj=select):
    setNm = cmds.polyNormal(nm=True)
    
    
setNm()