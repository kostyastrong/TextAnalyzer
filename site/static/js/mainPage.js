var divs = document.getElementsByClassName('book-title');
const title_lim = 18;
for (var i = 0; i < divs.length; ++i) {
    if (divs[i].innerHTML.length < title_lim) continue;
    divs[i].innerHTML = divs[i].innerHTML.substring(0, title_lim) + '...';  // we may use here href=
}

var divs = document.getElementsByClassName('book-title');
const title_lim = 18;
for (var i = 0; i < divs.length; ++i) {
    if (divs[i].innerHTML.length < title_lim) continue;
    divs[i].innerHTML = divs[i].innerHTML.substring(0, title_lim) + '...';  // we may use here href=
}

function shorterByTag(tag, lim) {
    var divs = document.getElementsByClassName(tag);
    for (var i = 0; i < divs.length; ++i) {
        if (divs[i].innerHTML.length < lim) continue;
        divs[i].innerHTML = divs[i].innerHTML.substring(0, lim) + '...';  // we may use here href=
    }
}