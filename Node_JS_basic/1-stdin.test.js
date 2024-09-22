const { exec } = require('child_process');
const assert = require('assert');

describe('1-stdin.js', function() {
  it('the user is entering a name', function(done) {
    const name = 'Guillaumeh';
    const expectedOutput = `Welcome to Holberton School, what is your name?\nYour name is: ${name}\r\nThis important software is now closing`;

    const child = exec(`echo "${name}" | node 1-stdin.js`, (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }

      // Trim whitespace for comparison
      assert.strictEqual(stdout.trim(), expectedOutput.trim());
      done();
    });

    child.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });
  });
});
