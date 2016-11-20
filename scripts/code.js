var loggedIn = false;;

//Login window validation
function loginValidation(){
	var usernameL = document.getElementById("usernameLogin").value;
	var passwordL = document.getElementById("passwordLogin").value;

	if(usernameL == "admin" && passwordL == "admin"){
		loggedIn = true;
		document.getElementById("profile").style.display = 'block';
	}
	
	if(loggedIn == true){
	}
}
