function getListStudentIds(students) {
// Check if the argument is an array
  if (Array.isArray(students)) {
    // Use map to extract the id from each student object
    return students.map((student) => student.id);
  }

  // Return an empty array if the argument is not an array
  return [];
}

export default getListStudentIds;
