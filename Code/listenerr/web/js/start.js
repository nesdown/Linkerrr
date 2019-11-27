async function selectAudioFile() {
  let audioName = await eel.select_audio_file()();
  document.getElementById('audiofiles').value = audioName;
}

async function selectAudioTemplate() {
  let audioTemplateName = await eel.select_audio_template()();
  document.getElementById('audiotemplates').value = audioTemplateName;
}

eel.expose(handleResultInput)
function handleResultInput() {
  return(document.getElementById('result-name').value);
}

eel.expose(handleResultInput)
function handleSoundInterference() {
  return(document.getElementById('result-interference').value);
}

function startAnalysis() {
  resultName = handleResultInput();
  soundInterference = handleSoundInterference();

  audioName = document.getElementById('audiofiles').value;
  audioTemplate = document.getElementById('audiotemplates').value;
  eel.start_analysis(audioName, audioTemplate, resultName, soundInterference);
}

eel.expose(updateConsole)
function updateConsole(textToUpdate){
  currentData = document.getElementById('console-text').innerHTML;
  console.log(currentData);

  if (currentData == "")
    document.getElementById('console-text').innerHTML = textToUpdate;
  else
    document.getElementById('console-text').innerHTML = currentData + "<br/>" + textToUpdate;

  console.log("Successfully Updated");
}

eel.expose(showResults)
function showResults() {
  window.location.href = "result.html";
}

// This one updates console text all the time
window.setInterval(function() {
  var elem = document.getElementById('console-text');
  elem.scrollTop = elem.scrollHeight;
}, 1000);
