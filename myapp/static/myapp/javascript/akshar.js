//  code for previewing photo and sign

function previewImage(event, previewId) {
    var input = event.target;
    var previewContainer = document.getElementById(previewId);
    previewContainer.innerHTML = "";
    
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function(e) {
            var img = document.createElement('img');
            img.src = e.target.result;
            previewContainer.appendChild(img);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}


// result javascript 

$(document).ready(function() {
    $('#resultForm').on('submit', function(event) {
        event.preventDefault();
        
        // Placeholder for form data submission to backend
        // Assuming the backend returns the following result data
        const resultData = [
            { subject: 'Math', marks: 95 },
            { subject: 'Science', marks: 90 },
            { subject: 'English', marks: 85 }
        ];

        const classValue = $('#class').val();
        const rollNumberValue = $('#rollNumber').val();

        // Clear previous results
        $('#resultTableBody').empty();

        // Append new results
        resultData.forEach(data => {
            $('#resultTableBody').append(`
                <tr>
                    <td>${classValue}</td>
                    <td>${rollNumberValue}</td>
                    <td>${data.subject}</td>
                    <td>${data.marks}</td>
                </tr>
            `);
        });

        // Show result container
        $('#resultContainer').show();
    });
});