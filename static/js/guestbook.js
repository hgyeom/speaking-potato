// 로딩 완료시
$(function () {
    listing();
});

// 방명록 조회.
function listing() {
    fetch("/api/guestbook").then((res) => res.json()).then((data) => {
        let rows = data["result"]; //데이터 리스트 받아와서
        $(".guestBook_list").empty();
        rows.forEach((a) => {
            let name = a["name"];
            // let g_password = a["g_password"];
            let comment = a["comment"];
            let g_num = a["_id"];
            console.log(g_num)
            let temp_html = `
                            <div class="list_container"> 
                            <span class="guestBook_comment">${comment}</span>
                            <span class="guestBook_name">-${name}-</span>
                            <button class="guestBook_update custom-btn btn-1" onclick="update_check('${g_num}')">수정</button>
                            <button class="guestBook_delete custom-btn btn-1" onclick="guestBook_delete('${g_num}')">삭제</button>
                            </div>
                            <hr />
                            `;

            $(".guestBook_list").prepend(temp_html);
        });
    });
}

// 방명록 작성
function posting() {
    let name = $(".guestBook_id").val();
    let g_password = $(".guestBook_password").val();
    let comment = $(".guestBook_comment").val();

    let formData = new FormData();
    formData.append("name_give", name);
    formData.append("g_password_give", g_password);
    formData.append("comment_give", comment);

    fetch("/api/guestbook", { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        alert(data["msg"]);
        window.location.reload(); //화면중앙을 누르면 화면내에서 새로고침되도록
    });
}

//김무겸. 수정시 비밀번호 확인을 위한 스크립트. 조회 기능 구현 시 db에 확인하는 과정 삭제 예정. > 고려중
function update_check(g_num) {
        
    let g_password = prompt("비밀번호를 입력 해 주세요",)

    let formData = new FormData();

    console.log(g_num)
    formData.append("g_password_give", g_password);
    formData.append("g_num_give", g_num);

    fetch('/api/guestbook/check', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {

        if(data['result']) {
            let name = data['result'].name;
            let comment = data['result'].comment;
            let g_num = data['result']._id;
            
            $('.posting').removeClass('on');
            $('.update').addClass('on');
            $('.guestBook_update_id').attr('value',name);
            $('.guestBook_update_id').attr('g_num',g_num);
            $('.update_comment').attr('placeholder',comment);
        } else{
            alert(data['msg']);
        }
    })  
}


// 김무겸. 수정 .
$('.update_btn').click(() =>{

    let formData = new FormData();

    let name = $('.guestBook_update_id').val();
    let comment = $('.update_comment').val();
    let g_num = $('.guestBook_update_id').attr('g_num');

    //코멘트가 비어있으면(입력하지 않으면) placeholder의 값으로 한다. placeholder는 db에 저장되있던 comment
    if(comment == ''){
        comment = $('.update_comment').attr('placeholder');
    }

    formData.append("name_give", name);
    formData.append("comment_give", comment);
    formData.append("g_num_give", g_num);

    fetch('/api/guestbook', { method: "PUT", body: formData }).then((res) => res.json()).then((data) => {
        alert(data['msg']);
        // 새로고침
        window.location.reload();
    })
})

$('.cancel_btn').click( () => { 
    window.location.reload();
})

// 김무겸. 삭제 기능. 
function guestBook_delete(g_num){
    let g_password = prompt("비밀번호를 입력 해 주세요",)

    let formData = new FormData();

    formData.append("g_password_give", g_password);
    formData.append("g_num_give", g_num);

    fetch('/api/guestbook', { method: "DELETE", body: formData }).then((res) => res.json()).then((data) => {
        alert(data['msg']);
        window.location.reload();
    })  
}
