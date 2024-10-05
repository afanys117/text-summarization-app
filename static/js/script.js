function getSummary() {
    const inputText = document.querySelector('#inputText').value;

    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summary').innerText = data.summary;
    })
    .catch(error => console.error('Error:', error));
}

const sBtn = document.querySelector('#sBtn');

sBtn.addEventListener('click', getSummary);
