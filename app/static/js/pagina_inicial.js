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

