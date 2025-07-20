document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('RED_HEADER_ID').addEventListener('click', function() {
    document.querySelector('TARGET_SELECTOR').style.COLOR_PROPERTY = 'VALUE';
  });
});
