function shorterByTag(tag, lim) {
    var divs = document.getElementsByClassName(tag);
    for (var i = 0; i < divs.length; ++i) {
        let sent = divs[i].innerHTML.trim();
        divs[i] = sent;
        if (sent.length <= lim) continue;
        let short = sent.substring(0, lim);
        console.log('Short the sentence: ' + sent + ' to: ' + short);
        divs[i].innerHTML = sent.substring(0, lim) + '...';  // we may use here href=
    }
}

shorterByTag('book-title', 30)
shorterByTag('book-author', 30)

