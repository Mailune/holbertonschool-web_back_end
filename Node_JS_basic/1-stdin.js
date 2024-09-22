// Display a welcome message and ask for the user's name
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Listen for the 'readable' event on stdin (standard input)
process.stdin.on('readable', () => {
  // Read the user's input
  const input = process.stdin.read();

  // If the input is not null, display the user's name
  if (input !== null) process.stdout.write(`Your name is: ${input}`);
});

// Listen for the 'end' event on stdin (standard input)
process.stdin.on('end', () => {
  // Display a closing message
  process.stdout.write('This important software is now closing\n');
});
