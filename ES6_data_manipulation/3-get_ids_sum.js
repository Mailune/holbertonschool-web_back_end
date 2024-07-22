function getStudentIdsSum(students) {
  // Use reduce to sum up all the student IDs
  return students.reduce((sum, student) => sum + student.id, 0);
}

export default getStudentIdsSum;
