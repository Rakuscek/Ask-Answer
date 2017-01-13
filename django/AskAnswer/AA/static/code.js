var emailCorrect = false;
var passwordsCorrect = false;

function registrationValidation() {
	var email = document.getElementById("email").value;
	var pass1 = document.getElementById("passwordRegister1").value;
	var pass2 = document.getElementById("passwordRegister2").value;
	
	if(!validateEmail(email)){
		document.getElementById("email").style.background = "#B64747";
	} else {
		document.getElementById("email").style.background = "none";
		emailCorrect = true;
	}

	if(pass1 != pass2 || pass1 == "" || pass2 == "") {
		document.getElementById("passwordRegister1").style.background = "#B64747";
		document.getElementById("passwordRegister2").style.background = "#B64747";
	} else {
		document.getElementById("passwordRegister1").style.background = "none";
		document.getElementById("passwordRegister2").style.background = "none";
		passwordsCorrect = true;
	}
}

function validateEmail(email) {
	var re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	return re.test(email);
}