from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
def Tree (x,y,z):
    mc.setBlocks(x-1,y,z-1,x,y+5,z,17)
    mc.setBlocks(x-3,y+4,z-3,x+2,y+7,z+2,161)
    
    
for i in range(10):
    for f in range(10):
        for l in range(10):
        
            Tree(x+i*5,y+i*f,z+i*l)
        

        
        
        
        
              