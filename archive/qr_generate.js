const fs = require('fs');
const qrcode = require('qrcode');

run('exact-1000');
run('exact-2000');
run('exact-3000');
run('exact-4000');
run('exact-5000');

async function run(name) {
  const res = await qrcode.toDataURL(name);
  console.log(name, res);

  fs.writeFileSync('./qr.html', `<img src="${res}">`);
  console.log('Wrote to ./qr.html');
}
