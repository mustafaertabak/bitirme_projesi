const buttons = Array.from(document.getElementsByClassName("c_button"));
const contents = Array.from(document.getElementsByClassName("content_c"));

for (var i in buttons) {

    buttons[i].addEventListener("click", function() {
        var content_id = this.getAttribute("data-content");


        for (var j in contents) {
            contents[j].style.display = "none";
        }

        for (var k in buttons) {
            buttons[k].classList.remove("f-pro-sag-active");
        }
        
        this.classList.add("f-pro-sag-active");

        document.getElementById(content_id).style.display = "block";
    });
}

const file_input = document.getElementById("img-input");
const file_src = document.getElementById("img-name");
const img_warning = document.getElementById("img-w");

const up_btn = document.getElementById("up-btn");

const allowed_types = ["image/jpeg", "image/png"];

file_input.addEventListener("change", function() {

    img_warning.style.display = "none";

    var file = this.files[0];

    if (allowed_types.indexOf(file.type) > -1) {

        file_src.innerHTML = this.files[0].name;

        up_btn.style.display = "inline-block";

    } else {

        up_btn.style.display = "none";

        img_warning.style.display = "block";
        
        file_src.innerHTML = "";
        file_input.value = "";
    } 
});