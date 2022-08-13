#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[2]:


from flask import Flask,render_template,request


# In[3]:


import joblib


# In[4]:


app = Flask(__name__)


# In[5]:


@app.route("/",methods=["GET","FOST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        pred2 = model2.predict([[rates]])
        return(render_template("index.html",result=pred1,result2=pred2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:


__name__


# In[ ]:




