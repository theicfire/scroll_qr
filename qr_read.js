const request = require("request"); // https://github.com/request/request
const PNG = require('pngjs').PNG; // https://www.npmjs.com/package/pngjs
const jsQR = require("jsqr");
const fs = require('fs');
const jpeg = require('jpeg-js');

const files = fs.readdirSync('frames').sort((a, b) => {
    const a_num = a.split('.')[0].split('frame')[1]
    const b_num = b.split('.')[0].split('frame')[1]
    return parseInt(a_num) > parseInt(b_num) ? 1 : -1;
});
function get_frame_location(fpath) {
    let jpegData = fs.readFileSync(fpath);
    let img = jpeg.decode(jpegData);
    let qr_res = jsQR(img.data, img.width, img.height);
    if (qr_res && qr_res.location) {
        console.log(fpath, qr_res.location.topLeftCorner.y);
    } else {
        console.log('Could not find in', fpath);
    }
}
files.forEach(fname => {
    get_frame_location(`frames/${fname}`);
});




//fs.createReadStream('double_qr.png')
    //.pipe(new PNG({
        //filterType: 4
    //}))
    //.on('parsed', function() {
        //console.log(this.data);
        //console.log(jsQR(this.data, this.width, this.height));
    //});
