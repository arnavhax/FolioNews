
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



document.addEventListener("DOMContentLoaded", function() {
    // Function to show loader and hide button
    function showLoader(button, loaderId) {
      button.style.display = 'none';
      document.getElementById(loaderId).style.visibility = 'visible';
    }
  
    // Handle saveStockForm submission
    document.getElementById("saveStockForm").addEventListener("submit", function(event) {
      showLoader(document.getElementById("submit_button"), "loader");
    });
  
    // Handle updateForm submission
    document.getElementById("updateForm").addEventListener("submit", function(event) {
      showLoader(document.getElementById("update_button"), "loader");
    });
  });
  