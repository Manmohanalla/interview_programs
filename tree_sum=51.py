#            5x       -> sum =   10
#       1         16x     -> sum = 
#   90    45    2    30  -> sum = 0
  
#   sum=51?  5 -> 1 -> 45   (1)
#            5 -> 16 -> 30  (2)
  
class tree(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

  def hasPathSum(self, root, sum,lst=[]):
    
    '''
    if root.getLeftChild() == None and root.getRightChild() == None:
        return getRootValue(root)
    else:
        leftSum = hasPathSum(root.getLeftChild())
        rightSum = hasPathSum(root.getRightChild())
        
    if lefSum >
    '''
  
    if root.left == None and root.righ == None and root.val == sum:
      return True
    
hex.append(hex(i)[2:].upper())          path =  lst.append(root.left.val)
    if self.hasPathSum(root.left, sum - root.val, path):
        return True,path
    if not root.right.val > sum-root.val:
      path = lst.append(root.right.val)
      if self.hasPathSum(root.right, sum - root.val, path):
        return True,path
    return False
