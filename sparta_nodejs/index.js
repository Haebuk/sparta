const express = require('express')
const app = express()
const port = 3000

const goodsRouter = require('./routes/goods');
const usersRouter = require('./routes/user');

app.use(express.urlencoded({extended: false})) // 나중에 씀
app.use(express.json())
app.use(express.static('public')); // http://localhost:3000/4848.jpg static이 public 폴더안에 동일한 파일이 있는지 체크후 파일 자체를 화면에 응답

app.use('/goods', goodsRouter)
app.use('/user', usersRouter)


// 미들웨어: 요청 전 선처리
// next()로 다음 미들웨어로 넘김. response를 만나면 요청한 브라우저로 연결 
app.use((req, res, next) => {
  console.log(req);
  next();
});

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs'); // ejs를 사용

app.get('/test', (req, res) => {
  let name = req.query.name; // 쿼리스트링으로 넘기기 
  // ex: http://localhost:3000/test?name=bob
  res.render('test', {name}); // send ... 대신 render(파일명) test파일에 있는 내용이 그려진다
})

app.get('/detail', (req, res) => { // detail: 브라우저상에서 이름
  res.render('detail'); // detail: ejs 파일 이름
})

app.get('/home', (req, res) => {
  res.render('index');
})

app.get('/', (req, res) => {
  res.send('<!DOCTYPE html>\
  <html lang="en">\
  <head>\
      <meta charset="UTF-8">\
      <meta http-equiv="X-UA-Compatible" content="IE=edge">\
      <meta name="viewport" content="width=device-width, initial-scale=1.0">\
      <title>Document</title>\
  </head>\
  <body>\
      Hi. I am with html<br>\
      <a href="/hi">Say Hi!</a>\
  </body>\
  </html>')
})

// app.get('/goods/list', (req, res) => {
//   res.send('상품 목록 페이지')
// })

// app.get('/goods/detail', (req, res) => {
//   res.send('상품 상세 페이지')
// })

// app.get('/user/login', (req, res) => {
//   res.send('로그인 페이지')
// })

// app.get('/user/register', (req, res) => {
//   res.send('회원가입 페이지')
// })

app.listen(port, () => {
  console.log(`listening at http://localhost:${port}`)
})