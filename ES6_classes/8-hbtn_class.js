class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Method called when the object is converted to a number
  valueOf() {
    return this._size;
  }

  // Method called when the object is converted to a string
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
