class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Use the Reflect.construct function to create a new instance of the current class
  // without passing the constructor arguments, leaving the attributes undefined.
  cloneCar() {
    return Reflect.construct(this.constructor, []);
  }
}

export default Car;
