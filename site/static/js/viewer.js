function getCookie(name) {
	var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}

function get_info(word){
    var elem = "<div class=\"toast fade show\" style=\"position: absolute;\" role=\"alert\" aria-live=\"assertive\" aria-atomic=\"true\">\
    <div class=\"toast-header\">\
      <button type=\"button\" class=\"ml-2 mb-1 close\" data-dismiss=\"toast\" aria-label=\"Close\">\
        <span aria-hidden=\"true\">&times;</span>\
      </button>\
    </div>\
    <div class=\"toast-body\">\
      Hello, world! This is a toast message.\
    </div>\
    </div>";
    word.innerHTML += elem;
}


$.ajax({
    url: 'http://localhost:5000/ajax',
    data: getCookie("current"),
    dataType: 'text',
    success: function(data) {
      var mydiv = document.getElementById("text_maker");
      
      var txt = data.replace(/\r?\n/g, ' '); 
      txt = txt.split(' ');
      var id = 0;
      for(var i=0; i<txt.length; ++i){
          var span = document.createElement('span');
          //span.innerHTML = txt[i] + " ";
          var mt = document.createElement('text');
          mt.setAttribute("id", "id"+id);
          mt.innerHTML = txt[i] + " ";
          mt.onclick = get_info(span); 
          //span.setAttribute("onclick", "get_info(this);");
          span.appendChild(mt);
          //span.setAttribute("onclick", "alert('"+txt[i]+"');");
          //span.setAttribute("onclick", "get_info(this);");
          mydiv.appendChild(span);
      }
    }
});