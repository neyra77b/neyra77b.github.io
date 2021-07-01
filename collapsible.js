//window.onload = function(){ 
 // }


window.onload = function() {
	/* Javascript for collapsible */
	var coll = document.getElementsByClassName("collapsible");
  var i;
  
  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }

	/* Javascript for Citations */
	var modal13 = document.getElementById("myModal13");
	var modal14 = document.getElementById("myModal14");
	var modal15 = document.getElementById("myModal15");
	var btn13 = document.getElementById("btn13");
	var btn14 = document.getElementById("btn14");
	var btn15 = document.getElementById("btn15");
	var span13 = document.getElementById("span13");
	var span14 = document.getElementById("span14");
	var span15 = document.getElementById("span15");
	
	btn13.onclick=function() {
		modal13.style.display="block";
	}
	btn14.onclick=function() {
		modal14.style.display="block";
	}
	btn15.onclick=function() {
		modal15.style.display="block";
	}
	
	span13.onclick=function(){
		modal13.style.display="none";
	}
	span14.onclick=function(){
		modal14.style.display="none";
	}
	span15.onclick=function(){
		modal15.style.display="none";
	}
	
	window.onclick=function(event) {
		if (event.target == modal13) {
			modal13.style.display = "none";
		}
		if (event.target == modal14) {
			modal14.style.display = "none";
		}
		if (event.target == modal15) {
			modal15.style.display = "none";
		}
	}
}
