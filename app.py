from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.9us23my.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guestbook')
def guestbook():
    return render_template("guestbook.html")

# #방명록 등록
# @app.route("/api/guestbook", methods=["POST"])
# def bucket_post():
#     name_receive = request.form['name_give']
#     g_password_receive = request.form['password_give']
#     comment_receive = request.form['comment_give']
    
#     doc = {
#             'name':name_receive,
#             'g_password':g_password_receive,
#             'comment':comment_receive,
#             'g_num':len(list(db.potato.find({})))
#         }
#     db.potato.insert_one(doc)
#     return jsonify({'msg': 'POST 연결 완료!'})
    

#수정을 위한 조회
@app.route("/api/guestbook/check", methods=["POST"])
def potato_update_check():
    g_password_receive = request.form['g_password_give']
    g_num_receive = int(request.form['g_num_give'])
    guestbook = db.potato.find_one({'g_num':g_num_receive,'g_password':g_password_receive},{'_id':False})
    if guestbook:
        return jsonify({'result':guestbook})
    else :
        return jsonify({'msg':'비밀번호를 확인해주세요'})


#방명록 수정
@app.route("/api/guestbook", methods=["POST"])
def potato_update():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    g_num_receive = int(request.form['g_num_give'])
    print("이름 : ",name_receive)
    print("코멘트 : ",comment_receive)
    print("번호 : ",g_num_receive)

    db.potato.update_one({'g_num':g_num_receive},
                        {'$set':{
                                    'name':name_receive,
                                    'comment':comment_receive
                                }
                        })
    return jsonify({'msg': '수정완료!'})



#방명록 조회
# @app.route("/api/guestbook", methods=["GET"])
# def bucket_get():
#     return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)