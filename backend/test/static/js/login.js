async function login() {
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');

    if (id.value == "" || pw.value == "") {
        alert("아이디 혹은 비밀번호를 확인해주세요.");
    } else {
        const options = {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body : JSON.stringify({
                userID : id.value,
                userPW : pw.value,
            })
        }
        await fetch("http://127.0.0.1:1398/login/", options)
            .then(function (response){
                let check = response.headers.get("check");
                // Login success
                if (check == "True"){
                    response.text().then((html) => document.write(html));
                } else{ // Login False
                    id.value = "";
                    pw.value = "";
                    alert("로그인에 실패했습니다.\n아이디 혹은 비밀번호를 다시 확인해보세요.");
                }
            })
            .catch((error) => console.log(error));
    }
}