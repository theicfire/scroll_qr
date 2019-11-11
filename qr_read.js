request = require("request"); // https://github.com/request/request
png = new (require('pngjs').PNG)(); // https://www.npmjs.com/package/pngjs
jsQR = require("jsqr");

request({
  uri: "https://www.dropbox.com/s/c6dqxuv8qnvc098/Screenshot%202019-11-11%2015.40.45.png?dl=1",
  encoding: null // Force null encoding to get data as a buffer
}, function(err, resp, body) { // Download the image
  if(err) {
    console.error(err);
    process.exit(1);
  }
  png.parse(body, function(err, decodedPng) { // Parse the png
    if(err) {
      console.error(err);
      process.exit(1);
    }
    // Use jsQR to decode it
    console.log(jsQR(decodedPng.data, decodedPng.width, decodedPng.height))
  });
});
