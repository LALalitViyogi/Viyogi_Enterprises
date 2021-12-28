from logging import debug
from flask import Flask,render_template, request, redirect
import sqlite3 as sql
import json

app = Flask(__name__)

img=["viyogi_notes.png","adi_image_logo.png","covid_logo.png","express_calcy_logo.png",
"aditya_secura_logo.png","vidat_logo.png","chekaut_logo.png","inserminal_logo.png"]

product=["Viyogi Notes","Adi Images","Covid Data","Express-Calcy","Aditya Secura",
"ViDaT Tool","CheKaut","Inserminal"]

link=["http://www.google.com/","http://www.github.com/","#","https://facebook.com",
"viyogilearnings.blogspot.com","#","#","#"]
color=["255,138,101","255,202,40","102,187,106","41,182,246",
"240,98,146","60,150,85","159,168,218","197,225,165"]

main_page_product=[2,3,1,5,6,4]

def update(products):  ## indices of all product that should be on main page
    global img
    new_product=[2,3,5,7,6,1]
    if type(products)== type(list()) and products is not None:
        indices=list()
        for product in products:
            indices.append(img.index(product))
        return indices
    else:
        return new_product

def Login():
    pass
@app.route('/')
def main():
    return render_template('home.html',imgs=img,len=main_page_product,links=link)

@app.route('/adlog')
def logpage():
    
    return render_template('login.html')

@app.route('/contact')
def cont():
    return render_template('contact.html')

@app.route('/signup', methods = ['POST'])
def signup():
    name = request.form['name']
    mail = request.form['email']
    print("The Name is "+ str(name),end="\n")
    print("And Email is "+ str(mail),end="\n")
    return redirect('/product')

@app.route('/product')
def products():
    return render_template('product.html',products=product,links=link,colors=color,imgs=img ,len=len(img))

@app.route('/project')
def projects():
    return render_template('project.html',imgs=img,len=main_page_product,links=link, products=product,colors=color)

@app.route('/skills')
def skill():
    return render_template('skills.html')

@app.route('/assessments')
def assess():
    return render_template('assessments.html')

if "__name__"=="__main__":
    app.run(debug=True)
