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

  // Disable the ESLint rule for this method
  /* eslint-disable-next-line class-methods-use-this */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

export default Building;
