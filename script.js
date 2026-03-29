async function fetchData() {
    const res = await fetch("/data");
    const data = await res.json();

    const table = document.getElementById("riskTable");
    table.innerHTML = `<tr>
        <th>App</th>
        <th>Connections</th>
        <th>Score</th>
        <th>Level</th>
        <th>Reason</th>
        <th>Suggestion</th>
    </tr>`;

    data.forEach(app => {
        let row = table.insertRow();
        row.insertCell(0).innerText = app.app;
        row.insertCell(1).innerText = app.connections;
        row.insertCell(2).innerText = app.score;
        row.insertCell(3).innerHTML = `<span class="${app.level.toLowerCase()}">${app.level}</span>`;
        row.insertCell(4).innerText = app.reason;
        row.insertCell(5).innerText = app.suggestion;
    });
}

setInterval(fetchData, 5000);
fetchData();
