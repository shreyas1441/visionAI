function submitForm() {
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;

    if (!latitude || !longitude) {
        alert('Please enter both latitude and longitude.');
        return;
    }

    fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'latitude': latitude,
            'longitude': longitude
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                document.getElementById('result').textContent = `Error: ${data.error}`;
            } else {
                document.getElementById('result').textContent = `Prediction: ${data.prediction}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').textContent = 'Error retrieving prediction.';
        });
}
