from flask import Flask, render_template
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/tc/')
def testcase():
    return render_template('testcase.html')

@app.route('/tc/<int:tc_id>')
def testcaseone(tc_id):
    return 'Hello, %d' % tc_id

@app.route('/ts/')
def testset():
    return render_template('testset.html')

@app.route('/ts/<int:ts_id>')
def testsetone(ts_id):
    return 'Hello, %d' % ts_id



if __name__ == '__main__':
   app.run()
