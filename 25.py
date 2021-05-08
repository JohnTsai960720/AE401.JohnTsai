from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
def Tree (x,y,z):
    mc.setBlocks(x-3,y+18,z-3,x+2,y+22,z+2,161)
   
    mc.setBlocks(x-1,y,z-1,x,y+20,z,17)
    
for i in range(0,50,5):
    for f in range(0,50,5):
         for p in range(0,41,20):
   
             Tree(x+i,y,z)
             Tree(x+i,y,z)
             Tree(x+i,y,z)
             Tree(x+i,y,z)
             Tree(x+i,y,z)
             Tree(x+i,y,z)
              
                  