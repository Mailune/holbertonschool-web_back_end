const fs = require('fs');

function countStudents(filePath) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(filePath, 'utf8');
    // Split the lines by newline character
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Check if there are any students
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Remove the header and create an array for the students
    const students = lines.slice(1).map((line) => {
      const [firstname, , , field] = line.split(','); // Ignore lastname and age
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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
