function set_like(like_name) {

    let formData = new FormData();

    formData.append("likename_give", like_name);
    
    fetch('/api/like', { method: "PUT", body: formData }).then((res) => res.json()).then((data) => {
        alert(data['msg']);
    })
}

