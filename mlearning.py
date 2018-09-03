
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('train.csv')


# In[3]:


df = df.fillna(0)


# In[4]:


df['NO_OCDE_AREA_GERAL']


# In[5]:


from sklearn import preprocessing


# In[6]:


le = preprocessing.LabelEncoder()


# In[7]:


le.fit(df['NO_OCDE_AREA_GERAL'])


# In[8]:


from datetime import datetime as data


# In[9]:


df['DT_INGRESSO_CURSO'] = df['DT_INGRESSO_CURSO'].apply(lambda x: data.strptime(x, "%Y-%m-%d").toordinal())


# In[10]:


le.classes_


# In[11]:


df['NO_OCDE_AREA_GERAL'] = le.transform(df['NO_OCDE_AREA_GERAL'])


# In[12]:


df['NO_OCDE_AREA_GERAL']


# In[13]:


Y_df = df['NO_OCDE_AREA_GERAL']


# In[14]:


X_df = pd.get_dummies(df[['CO_CATEGORIA_ADMINISTRATIVA', 'CO_ORGANIZACAO_ACADEMICA', 'CO_TURNO_ALUNO', 'CO_GRAU_ACADEMICO', 'CO_MODALIDADE_ENSINO', 'CO_COR_RACA_ALUNO','IN_FINANC_ESTUDANTIL','IN_ING_CONVENIO_PECG', 'IN_SEXO_ALUNO', 'IN_MOBILIDADE_ACADEMICA', 'DT_INGRESSO_CURSO']])


# In[15]:


X = X_df.values


# In[16]:


Y = Y_df.values


# In[17]:


from sklearn.ensemble import ExtraTreesClassifier


# In[18]:


modelo = ExtraTreesClassifier()


# In[19]:


modelo.fit(X, Y)


# In[20]:


dt = pd.read_csv('test.csv')


# In[21]:


dt = dt.fillna(0)


# In[22]:


sx = dt['NU_ANO_ALUNO_NASC'].astype(str) + '-' + dt['NU_MES_ALUNO_NASC'].astype(str) + '-' + dt['NU_DIA_ALUNO_NASC'].astype(str)
sx = sx.apply(lambda x: data.strptime(x, "%Y-%m-%d").toordinal())
sx = pd.DataFrame(sx, columns=['nascimento'])
dt = dt.join(sx)


# In[23]:


dt['DT_INGRESSO_CURSO'] = dt['DT_INGRESSO_CURSO'].apply(lambda x: data.strptime(x, "%Y-%m-%d").toordinal())


# In[24]:


T_df = pd.get_dummies(dt[['CO_CATEGORIA_ADMINISTRATIVA', 'CO_ORGANIZACAO_ACADEMICA', 'CO_TURNO_ALUNO', 'CO_GRAU_ACADEMICO', 'CO_MODALIDADE_ENSINO', 'CO_COR_RACA_ALUNO','IN_FINANC_ESTUDANTIL','IN_ING_CONVENIO_PECG', 'IN_SEXO_ALUNO', 'IN_MOBILIDADE_ACADEMICA', 'DT_INGRESSO_CURSO']])


# In[25]:


resultado = modelo.predict(T_df.values)


# In[26]:


resultado


# In[27]:


resultado = le.inverse_transform(resultado)


# In[28]:


resultado


# In[29]:


dt2 = pd.read_csv('test.csv')


# In[30]:


s = pd.DataFrame(dt2['index'])


# In[31]:


r = pd.DataFrame(resultado, columns=['NO_OCDE_AREA_GERAL'])


# In[32]:


saida = s.join(r)


# In[33]:


saida.to_csv('answer.csv', encoding='utf-8', index=False)

