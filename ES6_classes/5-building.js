// 5-building.js
class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (new.target === Building) {
      throw new Error('Cannot instantiate abstract class Building');
    }
  }

  get sqft() {
    return this._sqft;
  }

  // Disable the ESLint rule for this specific method
  /* eslint-disable class-methods-use-this */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
  /* eslint-enable class-methods-use-this */
}

export default Building;
