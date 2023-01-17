// get the form so we can read what was entered in it.
const formElement = document.forms[0];
// add a 'listener' to wait for a submission of our form. When that happens run the code below.
formElement.addEventListener('submit', function(e) {
    // stop the form from doing the default action.
    e.preventDefault();
});