let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i, tablinks, slides, dots, imageNumberClass;
  tablinks = document.getElementsByClassName("nav_link");
  slides = document.getElementsByClassName("mySlides");
  dots = document.getElementsByClassName("slide-show-demo");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  if ((n == 1) || (n > slides.length)) { imageNumberClass = "tab1" }
  if (n == 2) { imageNumberClass = "tab2" }
  if ((n == 3) || (n < 1)) { imageNumberClass = "tab3" }
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "unset";
  dots[slideIndex-1].className += " active";
  document.getElementById(imageNumberClass).className += " active";
}
