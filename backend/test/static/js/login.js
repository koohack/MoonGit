async function login() {
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    console.log(id.value);
    console.log(pw.value);
    if (id.value == "" || pw.value == "") {
        alert("아이디 혹은 비밀번호를 확인해주세요.");
    } else {
        const options = {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body : JSON.stringify({
                key : 1,
                key1 : 2,
            })
        }

        await fetch("http://114.204.91.74:1398/")
            .then((response) => console.log(response))
            .then((data) => console.log(data))
            .catch((error) => console.log(error));
    }

}