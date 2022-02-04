function rere() {
    var text = document.getElementById("txt-window");
    alert(text.value);
    var t = document.createElement("span");
    t.style = "color : red;";
    t.innerHTML = text.value;
    document.body.appendChild(t);
}