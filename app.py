from lib2to3.pgen2.token import LESS
from flask import Flask, render_template, request, redirect, Markup, abort
import random, math



app = Flask(__name__)

dirForItem = {}
dirForOrder = {}


@app.get('/')
def event_form():
    return render_template('index.html')

    

@app.post('/Enter_Orders')
def registered_form():
    
    total = 0
    orderNum = str(random.randint(1000, 6000))
    
    value = request.form.get('botton')
    key1= request.form.get('quanity', type=int)


    

    if key1 is None:
        message2 = """<div class="alert alert-danger text-center" role="alert">Quanity Must Be Greater Than 0</div>"""
        return render_template('index.html', message2=Markup(message2))
    else:
        if value == 'Red':
            total = float(key1 * 1.25)
            
        elif value == 'Green':
            total = float(key1 * 3.75)
            
        else:
            total = float(key1 * 2.50)
                
        
        if request.form.get("checkbox"):
            total = (math.ceil(total))
        
        
    dirForItem[orderNum] = [orderNum, value, total, key1]
 
    return render_template('Enter_Orders.html', result=dirForItem)


    




@app.get('/Enter_Orders')
def register_user():

    if len(dirForItem) == 0:
        return render_template('Enter_Orders.html', result=dirForItem)

    return render_template('Enter_Orders.html', result=dirForItem)
     

@app.get('/delete')
def delete_form():
    delete = request.args.get('delete')
    del dirForItem[delete]
    return redirect('/Enter_Orders')

    
