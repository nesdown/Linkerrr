function returnBack() {
  window.location.href = "loading.html";
}

eel.expose(showCircles)
function showCircles(coincidence_count, accuracy, quality) {

  document.getElementsByClassName("stat1").innerHTML = '<div class="ldBar mainline label-center res1" data-value="' + coincidence_count + '" data-preset="circle"></div><p>Accuracy</p>';

  document.getElementsByClassName("stat2").innerHTML = '<div class="ldBar mainline label-center res2" data-value="' + accuracy + '" data-preset="circle"></div><p>Accuracy</p>';

  document.getElementsByClassName("stat3").innerHTML = '<div class="ldBar mainline label-center res3" data-value="' + quality + '" data-preset="circle"></div><p>Accuracy</p>';

}
