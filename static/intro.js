function openNav() {
    document.getElementById("menu_links").style.width = "250px";
  }
  
function closeNav() {
  document.getElementById("menu_links").style.width = "0";
}

function goToScreen() {
    var chosen = document.getElementById("dropdown")
    window.location.href = chosen.value
}

