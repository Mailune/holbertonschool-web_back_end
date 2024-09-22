const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    // Read the file asynchronously
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        return reject(new Error('Cannot load the database'));
      }

      // Split the lines by newline character
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Check if there are any students
      if (lines.length <= 1) {
        console.log('Number of students: 0');
        return resolve(); // Added return to avoid "Expected to return a value" error
      }

      // Remove the header and create an array for the students
      const students = lines.slice(1).map((line) => {
        const [firstname, , , field] = line.split(','); // Ignore unused variables 'lastname' and 'age'
        return { firstname, field };
      });

      // Count students by field
      const fieldCount = {};
      students.forEach((student) => {
        if (!fieldCount[student.field]) {
          fieldCount[student.field] = [];
        }
        fieldCount[student.field].push(student.firstname);
      });

      // Display the total number of students
      console.log(`Number of students: ${students.length}`);

      // Display students by field
      for (const [field, names] of Object.entries(fieldCount)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      return resolve(); // Added return to ensure the promise is always resolved
    });
  });
}

module.exports = countStudents;
