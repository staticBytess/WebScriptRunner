// Fetch logs every 1 second
async function fetchLogs() {
    const response = await fetch("/logs_raw"); // You need a Flask route returning raw logs
    const text = await response.text();
    const logBox = document.getElementById("log_box");
    logBox.textContent = text;
    logBox.scrollTop = logBox.scrollHeight; // scroll to bottom
}

setInterval(fetchLogs,1000); // refresh every second
fetchLogs(); // initial load