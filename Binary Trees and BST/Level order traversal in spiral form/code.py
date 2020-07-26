def printSpiral(root):
    stack1=[]
    stack2=[]
    
    if(root==None):
        return
    stack1.append(root)
    
    while(len(stack1)!=0 or len(stack2)!=0):
    
        while(len(stack1)!=0):
            top=stack1.pop(len(stack1)-1)
            
            if top.right:
                stack2.append(top.right)
                
            if top.left:
                stack2.append(top.left)
                
            print(top.data, end=' ')
            
        while(len(stack2)!=0):
            top=stack2.pop(len(stack2)-1)
            
            if top.left:
                stack1.append(top.left)
                
            if top.right:
                stack1.append(top.right)
                
            print(top.data, end=' ')
