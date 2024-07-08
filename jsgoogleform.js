
// Function to randomly click 3rd, 4th, or 5th element in each group of 5
function randomlyClickFive(elements) {
    // Iterate through the elements in chunks of 5
    for (var i = 0; i < elements.length; i += 5) {
        // Randomly choose an index between 2 and 4 (3rd, 4th, or 5th element)
        var randomIndex = Math.floor(Math.random() * 3) + 2; // 2, 3, or 4

        // Ensure the index doesn't exceed the group size
        if (i + randomIndex < elements.length) {
            elements[i + randomIndex].click(); // Simulate a click on the randomly chosen element
        }
    }
}
function randomlyClickTwo(elements) {
    // Iterate through the elements in chunks of 5
    for (var i = 0; i < elements.length; i += 5) {
        // Randomly choose an index between 2 and 4 (3rd, 4th, or 5th element)
        var randomIndex = Math.floor(Math.random() * 3) + 2; // 2, 3, or 4

        // Ensure the index doesn't exceed the group size
        if (i + randomIndex < elements.length) {
            elements[i + randomIndex].click(); // Simulate a click on the randomly chosen element
        }
    }
}


var next_btn = document.querySelector('.NPEfkd');
next_btn.click()

var spanElement = document.querySelector('span.certain:not(:empty):not(:has(*)):contains("Next")');
spanElement.click()

// wait for 1 second

setTimeout(function() { }, 1000);

var checkboxes1 = document.querySelectorAll('.ajBQVb');

setTimeout(function() { }, 1000);


// Select all elements with class '.eRqjfd'
var checkboxes = document.querySelectorAll('.eRqjfd');

// Call the function to randomly click elements
randomlyClickFive(checkboxes);