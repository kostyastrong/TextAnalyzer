var divs = document.getElementsByClassName('book-title');
const title_lim = 18;
for (var i = 0; i < divs.length; ++i) {
    if (divs[i].innerHTML.length < title_lim) continue;
    divs[i].innerHTML ='...';  // we may use here href=
}