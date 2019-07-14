// transparência da nav
window.onscroll = scroll;

function scroll() {
  let scrollTop = window.pageYOffset;
  if (scrollTop > 30) {
    try {
      document.getElementById('antes').id = 'depois'
    } catch (e) { 
      false 
    }
  } else {
    try {
      document.getElementById('depois').id = 'antes'
    } catch (e) { 
      false
    }
  }
}

// scroll

$('nav a').click(function(e){
  var id = $(this).attr('href'),
      targetOffset = $(id).offset().top,
      menuHeight = $('nav').innerHeight();
  $('html, body').animate({
      scrollTop: targetOffset - menuHeight
  }, 500);
});

// animação

// Debounce do Lodash
debounce = function(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

(function(){
let $target = $('.anime'),
    animationClass = 'anime-start',
    offset = $(window).height() * 3/4; 

function animeScroll() {
  let documentTop = $(document).scrollTop();

  $target.each(function() {
      let itemTop = $(this).offset().top - 750;
      if (documentTop > itemTop) {
        $(this).addClass(animationClass);
      } else {
        $(this).removeClass(animationClass);
      }
  })
}

animeScroll();

$(document).scroll(debounce(function(){
  animeScroll();
}, 200));
})();