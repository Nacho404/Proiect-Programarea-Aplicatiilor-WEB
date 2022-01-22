const endpoint = "http://127.0.0.1:5000/sign-up"

// functie pentru "success"
function success(response) {
    if (!response.ok) {
        throw response;
    }
    return response;
    
}

// ce sa faca in caz de "Success"
function onSuccess() {
    // window.location.href = signInPageUrl;
    const errorParagraph = document.querySelector("#message-sign-up");
    errorParagraph.innerText = "Contul a fost creeat cu succes! Multumim.";
}



// ce sa faca in caz de "Filure"
function onFailure(response) {
    return response.json().then(error);
}


// functie pentru cazul in care intampin erori
function error(response) {
    // get error paragraph 
    const errorParagraph = document.querySelector("#message-sign-up");
    errorParagraph.innerText = response.error;
    // alert(response.error);

    if(response.error == undefined){
        onSuccess();
    }
}

// functionalitate buton pentru SIGN UP
function signUp(){

    // extrag valorile din input fields
    const valuesOfInputs = {
        "first_name": document.getElementsByName("firstName")[0].value,
        "last_name": document.getElementsByName("lastName")[0].value,
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    };

    console.log(valuesOfInputs)
    // initializez parametri unui request POST catre API-ul de sign up
    const parameters = {
        body: JSON.stringify(valuesOfInputs),
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        }
    };  


    fetch(endpoint, parameters)
        .then(success)
        .then(onFailure)
        .catch(error);

    
    
    // function emailVerification(){
    //     email = {
    //         "email": document.getElementsByName("email")[0].value
    //     }


    //     const parameters = {
    //         body: JSON.stringify(email),
    //         method: "GET",
    //         mode: "cors",
    //         headers: {
    //             "Content-Type": "application/json"
    //         }
    //     };
        
    //     fetch("http://127.0.0.1:5000/sign-in", parameters)
    //         .then()
    
    
    // }
    

}



