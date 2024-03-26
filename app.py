#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import google.generativeai as palm
palm.configure(api_key='AIzaSyCOBhgDi-GwHGSmS-p3PN-RYj3eslN-7W0')
model = { 'model': "models/chat-bison-001"}

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
        return(render_template("index.html"))
    
@app.route("/main",methods=["GET","POST"])
def main():
    name=request.form.get('name')
    return(render_template("main.html",r=name))

@app.route("/palm_request",methods=["GET","POST"])
def palm_request():
    return(render_template("palm_request.html"))

@app.route("/palm_reply",methods=["GET","POST"])
def palm_reply():
    q = request.form.get("q")
    response = palm.chat(**model, messages=q)
    print(response.last)
    return(render_template("palm_reply.html",result=response.last))
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)


# In[ ]:





# In[ ]:




