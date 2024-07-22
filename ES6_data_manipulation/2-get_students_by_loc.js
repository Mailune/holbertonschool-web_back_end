function getStudentsByLocation(students, city) {
  // Use filter to create a new array with students located in the specified city
  return students.filter((student) => student.location === city);
}

export default getStudentsByLocation;
