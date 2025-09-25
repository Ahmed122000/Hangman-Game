

shape0 = """ 
 ____________
|/      |
|       |
|       |
|       |
|       
|      
|       
|      
|   
|____________
"""

shape1 = """
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|     
|       
|             
|   
|____________
"""

shape2 = """ 
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|       |
|       
|         
|        
|____________
"""

shape3 = """
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|      \\|
|       
|         
|        
|____________
"""

shape4= """
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|      \\|/
|
|     
|        
|____________
"""

shape5 = """
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|      \\|/
|       |
|      /  
|        
|____________
"""

winner = """

Winner \n 
       (_)
       \\|/
        |
       / \\

"""

loser = """ 
Loser 
 ____________
|/      |
|       |
|       |
|       |
|      (_) 
|      \\|/
|       |
|      / \\ 
|        
|___________

Game Over
"""
def get_shape(progress):

    if progress == 0: 
        return shape0    

    elif progress == 1: 
        return shape1

    elif progress == 2: 
        return shape2
        
    elif progress == 3: 
        return shape3

    elif progress == 4: 
        return shape4
        
    elif progress == 5:
        return shape5
    
    elif progress > 5:
        print("winner")
        return winner
    
    elif progress < 0: 
        return loser