function sendData() {

  let answer = document.getElementById("inputText").value;
  let output = document.getElementById("output");
  let button = document.querySelector("button");

  // Check if input is empty
  if (answer.trim() === "") {
    output.innerHTML = "⚠️ Please enter student answer!";
    return;
  }

  // Show loading state
  output.innerHTML = "Analyzing your answer...";
  button.innerText = "Analyzing...";
  button.disabled = true;

  fetch("https://127.0.0.1:5000/evaluate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      answer: answer
    })
  })
  .then(response => response.json())
  .then(data => {

    // Restore button
    button.innerText = "Analyze";
    button.disabled = false;

    // Show result nicely
    output.innerHTML = `
      <h3>📊 Score: ${data.score}</h3>
      <p style="color:red;"><b>❌ Mistakes:</b><br>${data.mistakes}</p>
      <p style="color:green;"><b>💡 Feedback:</b><br>${data.feedback}</p>
    `;
  })
  .catch(error => {

    button.innerText = "Analyze";
    button.disabled = false;

    output.innerHTML = "❌ Error connecting to server!";
    console.error(error);
  });
}