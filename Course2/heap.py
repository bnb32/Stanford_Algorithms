import numpy as np

class entry:
    def __init__(self,item='',key=''):
        self.key = key
        self.item = item
                
                
class heap:
    def __init__(self):
        self.Q = []
        self.item_index = {}
    
    def parent(self,i):
        if i==0: return 0
        return int(np.floor((i-1)/2))
    
    def children(self,i):
        return 2*i+1, 2*(i+1)
    
    def swap(self,i,j):
        e_i = self.Q[i]
        e_j = self.Q[j]
        self.Q[i] = e_j
        self.Q[j] = e_i
        self.item_index[e_j.item] = i
        self.item_index[e_i.item] = j
    
    def push(self,item,key):
        self.Q.append(entry(item=item,key=key))
        self.item_index[item] = len(self.Q)-1
        self.bubble_up(len(self.Q)-1)
        
    def pop(self):
        
        if len(self.Q)==1:
            e = self.Q.pop()
            self.item_index.pop(e.item)
        else:
            e = self.Q[0]
            self.item_index.pop(e.item)
            self.Q[0] = self.Q.pop()
            self.item_index[self.Q[0].item] = 0
            self.bubble_down(0)
        return e.item    
    
    def bubble_up(self,i):
        c_idx = i
        p_idx = self.parent(c_idx)
        
        while self.Q[p_idx].key > self.Q[c_idx].key:
            self.swap(p_idx,c_idx)
            c_idx = p_idx
            p_idx = self.parent(c_idx)    
   
    def bubble_down(self,i):
        
        p_idx = i
        c1, c2 = self.children(p_idx)
        
        while ((c1 < len(self.Q) and self.Q[p_idx].key > self.Q[c1].key) or 
               (c2 < len(self.Q) and self.Q[p_idx].key > self.Q[c2].key)):
            if c1 < len(self.Q) and c2 < len(self.Q):
                if self.Q[c1].key < self.Q[p_idx].key and self.Q[c2].key >= self.Q[p_idx].key:
                    self.swap(p_idx,c1)
                    p_idx = c1
                elif (self.Q[c2].key < self.Q[p_idx].key) and (self.Q[c1].key >= self.Q[p_idx].key):
                    self.swap(p_idx,c2)
                    p_idx = c2
                else:
                    if self.Q[c2].key < self.Q[c1].key:
                        self.swap(p_idx,c2)
                        p_idx = c2
                    else:
                        self.swap(p_idx,c1)
                        p_idx = c1
            elif c1 < len(self.Q):
                self.swap(p_idx,c1)
                p_idx = c1
            else:
                self.swap(p_idx,c2)
                p_idx = c2
            c1, c2 = self.children(p_idx)
        
    def update(self,item,key):
        
        idx = self.item_index[item]
        c1, c2 = self.children(idx)
        p_idx = self.parent(idx)
        
        self.Q[idx] = entry(item=item,key=key)
        
        if (idx == 0):
            if (key > self.Q[c1].key or key > self.Q[c2].key):
                self.bubble_down(idx)
        
        elif (idx == len(self.Q)-1):
            if (key < self.Q[p_idx].key):
                self.bubble_up(idx)
        else:
            if ((c1 < len(self.Q) and key > self.Q[c1].key) or 
               (c2 < len(self.Q) and key > self.Q[c2].key)):
                self.bubble_down(idx)
            elif (key < self.Q[p_idx].key):
                self.bubble_up(idx)

    def is_empty(self):
        if self.Q:
            return False
        return True
              
