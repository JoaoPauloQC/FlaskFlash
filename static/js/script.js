

const loginform = document.getElementById("loginform")

loginform.addEventListener('submit',(e) =>{
    
    

    console.log("oi")
    let name = document.getElementById("loginname")
    let email = document.getElementById("loginemail")
    console.log(name)
    console.log(email)
    let inputs = [name,email]
    console.log(inputs)
    


    validation = (wrong) => {
        wrong = wrong.slice(5)
        console.log("na validação")
        console.log(wrong + "validate")
        let toinsert = document.getElementById(wrong + "validate")
        console.log(toinsert)
        console.log(toinsert)
        toinsert.innerHTML = "Este campo é obrigatório"
        putOnScreen(wrong)
    }

    const putOnScreen = (wrong) =>{
        let toinsert = document.getElementById(wrong + "validate")
        if (toinsert.classList.contains("none")){
            toinsert.classList.remove("none")
        }
    }
    
    const byeOnScreen = (wrong) => {
        wrong = wrong.slice(5)
        
        let toRemove = document.getElementById(wrong + "validate")
        console.log("tem? " + toRemove.classList.contains("none") )
        if (toRemove.classList.contains("none") === false){
            toRemove.classList.add("none")
        }
    } 

    check = () => {
        console.log("na checagem")
        for (let i of inputs) {
            console.log(i.id)
            console.log(i === "")
            if (i.id !== "loginemail" ){
                console.log("to no if e sou" + i.id)
                if (i.value === ""){
                validation(i.id)
                }
                else{
                byeOnScreen(i.id)
                }

            }
            else{
                console.log("else email e ")
                console.log(i.value)
                
                if (!i.value.contains("@gmail.com")){
                    validation(i.id)
                    }
                    else{
                    byeOnScreen(i.id)
                    }
            }

        }

    }

    check()

    console.log(document.getElementsByClassName("none").length != 2)
    console.log(document.getElementsByClassName("none").length )

    if (document.getElementsByClassName("none").length != 2){
        e.preventDefault()
    }

})