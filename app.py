from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.9us23my.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

# 메인 페이지 
@app.route('/')
def home():
    return render_template('index.html')

# 팀원 소개 페이지
@app.route('/members')
def members():
    return render_template('members.html')

# 방명록 페이지
@app.route('/guestbook')
def guestbook():
    return render_template("guestbook.html")


# 이안진   
# 방명록 조회(Get)
@app.route("/api/guestbook", methods=["GET"])
def potato_get():
    all_guestbooks = list(db.potato.find({}, {'_id':False})) #dB상의 데이터들을 변수 all_guestbooks에 저장하고
    return jsonify({'result': all_guestbooks})  #클라이언트로 내려줌

# 방명록 등록  
@app.route("/api/guestbook", methods=["POST"])
def potato_post():
    name_receive = request.form['name_give']
    g_password_receive = request.form['g_password_give']
    comment_receive = request.form['comment_give']

    doc = {
            'name': name_receive,
            'g_password': g_password_receive,
            'comment': comment_receive,
            'g_num':len(list(db.potato.find({})))
    }
    db.potato.insert_one(doc)  #db에 데이터 저장
    return jsonify({'msg': '방명록 저장완료'})


# 김무겸
# 수정을 위한 조회
@app.route("/api/guestbook/check", methods=["POST"])
def potato_update_check():
    g_password_receive = request.form['g_password_give']
    g_num_receive = int(request.form['g_num_give'])
    guestbook = db.potato.find_one({'g_num':g_num_receive,'g_password':g_password_receive},{'_id':False})
    
    if guestbook:
        return jsonify({'result':guestbook})
    else :
        return jsonify({'msg':'비밀번호를 확인해주세요'})


# 방명록 수정
@app.route("/api/guestbook", methods=["PUT"])
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

# 방명록 삭제
@app.route("/api/guestbook", methods=["DELETE"])
def potato_delete():
    g_num_receive = int(request.form['g_num_give'])
    g_password_receive = request.form['g_password_give']
    
    # 데이터 찾기
    guestbook = db.potato.find_one({'g_num':g_num_receive,'g_password':g_password_receive},{'_id':False})
    
    # 찾은 데이터가 있으면 삭제하고 삭제완료 메시지를 보내준다. 없으면 비밀번호 확인 메시지를 보내준다.
    if guestbook:
        db.potato.delete_one({'g_num':g_num_receive,'g_password':g_password_receive})
        return jsonify({'msg':"삭제 완료"})
    else :
        return jsonify({'msg':'비밀번호를 확인해 주세요'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)