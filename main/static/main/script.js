document.getElementById('saveStockForm').addEventListener('submit', function(event) {
    console.log("event listner hit")
    event.preventDefault(); // Prevent the default form submission
    var form = this;
    var formData = new FormData(form);

    // Perform AJAX request to submit the saveStock form
    fetch(form.action, {
        method: form.method,
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    }).then(response => {
        if (response.ok) {
            // Form submitted successfully, now submit the update form
            document.getElementById('updateForm').submit();
        } else {
            // Handle the error response if needed
            console.error('Failed to submit saveStock form.');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});

document.querySelectorAll('.deleteStockForm').forEach(function(form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = new FormData(form);

        // Perform AJAX request to submit the deleteStock form
        fetch(form.action, {
            method: form.method,
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        }).then(response => {
            if (response.ok) {
                // Form submitted successfully, now submit the update form
                setTimeout(function() {
                    document.getElementById('updateForm').submit();
                }, 1000);
            } else {
                // Handle the error response if needed
                console.error('Failed to submit deleteStock form.');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });
});