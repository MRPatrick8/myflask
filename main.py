from flask import Flask, request
from datetime import datetime


app =  Flask('My App')
@app.route('/')
def index():
    return 'Hello, i made it! welcome here too!'

@app.route('/contact')
def Contact_page():
    return """
    <center><button>Go back Home</button>
    <h1> Contact me:</h1>
    <p>renepatrick978@gmail.com</p>
    <p>0789819883</p></center>
    """
@app.route('/date')
def date_page():
    date =  str(datetime.now())
    return f"today is:{date}"

@app.route('/birth', methods = ['POST','GET'])
def calc():
    if request.method == 'GET':
        return """
            <form action = '/birth' method = 'POST'>
            <input type = 'number' name = 'birthyear' placeholder = 'Birth Year eg 1900'/>
            <button type = 'submit'>Submit</button>   
            </form>
            """
    elif request.method == 'POST':
        return f"""
        <form action = '/birth' method = 'POST'>
            <input type = 'number' name = 'birthyear' placeholder = 'Birth Year eg 1900'/>
            <button type = 'submit'>Submit</button>   
            </form>
        from your submission your age is {2022- int(request.form.get('birthyear'))}"""
        










    # # if request.method == 'POST':
    # #    return f"you declared your age as {request.form.get('birthyear')}"
    # if request.method == 'GET':
    #     return """
    #     <form action = '/birth' method = 'POST'>
    #     <input type = 'number' name = 'birthyear' placeholder = 'Birth Year eg 1900'>
    #     <button type = 'submit'>Submit</button>   
    #     </form>
    #     """
    # # date =  str(datetime.now())
    # # return f"today is:{date}"



if __name__ == '__main__':
    app.run()