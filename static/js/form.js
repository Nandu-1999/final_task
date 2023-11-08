const form = document.getElementById("app-form");
const popup = document.getElementById("popup");
const overlay = document.getElementById("overlay");
const closePopup = document.getElementById("closePopup");

form.addEventListener('submit',function(event) {
   event.preventDefault();

   popup.style.display = 'block';
   overlay.style.display = 'block';
});

closePopup.addEventListener('click',function() {

   popup.style.display = 'none';
   overlay.style.display = 'none';
});