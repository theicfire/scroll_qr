const jsQR = require("jsqr");
const fs = require('fs');
const jpeg = require('jpeg-js');

let jpegData = fs.readFileSync('frame2.jpg');
let img = jpeg.decode(jpegData);
console.log(jsQR(img.data, img.width, img.height));
