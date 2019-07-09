window.onscroll = scroll;

function scroll() {
  let scrollTop = window.pageYOffset;
  if (scrollTop > 100) {
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