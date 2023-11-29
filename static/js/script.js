const yearSelector = document.getElementById('year');
const placementRecord = document.getElementById('placement-record');

// Load placement data from JSON file
fetch('placement_data.json')
  .then(response => response.json())
  .then(data => {
    // Display placement data for the default year (2022)
    displayPlacementData(data['2022']);

    // Add event listener to year selector
    yearSelector.addEventListener('change', event => {
      const selectedYear = event.target.value;
      displayPlacementData(data[selectedYear]);
    });
  });

// Display placement data for a given year
function displayPlacementData(data) {
  placementRecord.innerHTML = '';

  data.forEach(record => {
    const card = document.createElement('div');
    card.classList.add('placement-card');

    const companyName = document.createElement('h2');
    companyName.textContent = record.companyName;

    const jobRole = document.createElement('p');
    jobRole.textContent = `Job Role: ${record.jobRole}`;

    const salary = document.createElement('p');
    salary.textContent = `Salary: ${record.salary}`;

    card.appendChild(companyName);
    card.appendChild(jobRole);
    card.appendChild(salary);

    placementRecord.appendChild(card);
  });
}
