from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']  #title_give 가 있는지 확인한다. 있으면 title_receive 에 담는다.
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'}) #js 의 data로 들어간다.

# @app.route('/test', methods=['GET'])  #get요청으로 /test 라는 창구로 들어온다.
# def test_get():
#    title_receive = request.args.get('title_give')
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!!!','msg2':'하하하'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)