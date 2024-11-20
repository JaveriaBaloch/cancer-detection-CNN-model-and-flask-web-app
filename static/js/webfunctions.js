    const form = document.getElementById('upload-form');
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const fileInput = document.getElementById('file');
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);

            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            document.getElementById('prediction-result').textContent = data.prediction;

            if (data.image_url) {
                const imgElement = document.createElement('img');
                imgElement.src = data.image_url;
                imgElement.alt = "Uploaded Image";
                document.getElementById('image-result').innerHTML = ''; // Clear previous image
                document.getElementById('image-result').appendChild(imgElement);
            }
        });
 document.querySelector('.nav-link[href="#Contact_Me"]').addEventListener('click', function(e) {
    e.preventDefault();
    const contactSection = document.getElementById('Contact_Me');
    contactSection.classList.toggle('show');
});

document.getElementById('close-btn').addEventListener('click', function() {
    const contactSection = document.getElementById('Contact_Me');
    contactSection.classList.remove('show');
});
