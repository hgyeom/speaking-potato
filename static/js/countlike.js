//로딩시
$(function () {
    like();
});


//응원하기 
function set_like(like_name) {
    let formData = new FormData();

    formData.append("likename_give", like_name)
    
    fetch('/api/like', { method: "PUT", body: formData }).then((res) => res.json()).then((data) => {
        alert(data['msg']);
        window.location.reload();
    })
}

//응원하기 조회
function like() {
    fetch("/api/like").then((res) => res.json()).then((data) => {
        let rows = data["result"];
        
        $('#mugyeom').text(rows[0].like);
        $('#anjin').text(rows[1].like);
        $('#songju').text(rows[2].like);
        $('#jaeyoung').text(rows[3].like);
        $('#dayeon').text(rows[4].like);
        
    });
}