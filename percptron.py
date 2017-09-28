
# coding: utf-8

# # Perceptron Simples

# In[1]:


from random import choice
from numpy import array, dot, random
from pylab import plot
get_ipython().magic('matplotlib inline')


# In[2]:


gatilho = lambda x: 0 if x < 1 else 1


# In[3]:


treino = [ 
    (array([0,0,0]), 1),
    (array([0,0,1]), 1),
    (array([0,1,0]), 1),
    (array([0,1,1]), 1),
    (array([1,0,0]), 1),
    (array([1,0,1]), 1),
    (array([1,1,0]), 1),
    (array([1,1,1]), 0),
]


# In[4]:


peso = random.rand(3)
baias = random.rand(1)
taxa = 0.05
n = 1000


# In[6]:


erros = [] 

for i in range(n): 
    x, experado = choice(treino)
    resultado = dot(peso, x) + baias
    erro = experado - gatilho(resultado) 
    erros.append(erro)
    print("x = %s peso = %s baias = %s experado = %s y = %s e = %s" % (x, peso, baias, experado, gatilho(resultado), erro))
    if erro != 0:
        peso += taxa * erro * x
        baias += taxa * erro * baias
    
plot(erros)

