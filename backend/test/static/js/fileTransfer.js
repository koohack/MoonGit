async function send(){
    let fileElement = document.getElementById("fileUpload");
    let data = new FormData();
    let files = fileElement.files;

    for (let i = 0; i < files.length; i++){
        data.append('file'+i, files.item(i), files.name);
    }

    const options = {
        method : "POST",
        body : data,
    };

    await fetch("http://127.0.0.1:1398/upload/", options)
        .catch((error) => console.log(error));
}

async function temp(){

    const options = {
        method: "POST",
        header : {
            "Content-Type" : "application/json",
        },
        body : JSON.stringify({
            whatWeNeed : "ini",
        }),
    }

    await fetch("http://127.0.0.1:1398/sendfile/", options)
        .then(function (response){
            var temp = response.body.getReader().read();

            console.log(temp)
        })
        .catch((error) => console.log(error))

}