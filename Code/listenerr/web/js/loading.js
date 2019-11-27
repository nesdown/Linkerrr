let status = 0;

$(document).ready(function ()
  {
    updateLoading(5);
  }
)

function updateLoading(interv) {
  if (status > 100) {
    console.log("Finished!");
    window.location.href = "start.html"
  }

  else {
    let bar1 = new ldBar("#loadingBar");
    // let bar = $('#loadingBar').ldBar;
    bar1.set(parseInt(status));

    status = status + parseInt(interv);
    console.log(status);
    // 300 for normal
    setTimeout(updateLoading, 300, interv);
  }
}
