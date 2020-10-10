from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guest'}
    return '''
<html>
    <head>
        <title>Home Page - DeltaLink</title>
    </head>
    <body>
        <h1>Welcome, ''' + user['username'] + '''!</h1>
    </body>
</html>'''