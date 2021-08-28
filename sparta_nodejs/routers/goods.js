const express = require("express");
const Goods = require("../schemas/goods");
const Cart = require("../schemas/cart");
const router = express.Router();

router.get("/goods", async (req, res, next) => {
  try {
    const { category } = req.query;
    const goods = await Goods.find({ category }).sort("-goodsId"); // category가 있으면 category에 맞는 애만 가져옴. goodsId 기준 정렬해서 가져옴
    res.json({ goods: goods }); // json 형식으로 내려줌
  } catch (err) {
    console.error(err);
    next(err);
  }
});

router.get("/goods/:goodsId", async (req, res) => { //goodsId 변수가 들어옴
  const { goodsId } = req.params;
  goods = await Goods.findOne({ goodsId: goodsId }); // 딱 하나만
  res.json({ detail: goods });
});

router.post('/goods', async (req, res) => {
    const { goodsId, name, thumbnailUrl, category, price } = req.body;
  
    isExist = await Goods.find({ goodsId }); // 중복 체크
    if (isExist.length == 0) { // 없으면 생성
      await Goods.create({ goodsId, name, thumbnailUrl, category, price });
    }
    res.send({ result: "success" });
  });

router.post("/goods/:goodsId/cart", async (req, res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;

  isCart = await Cart.find({ goodsId });
  console.log(isCart, quantity);
  if (isCart.length) {
    await Cart.updateOne({ goodsId }, { $set: { quantity } });
  } else {
    await Cart.create({ goodsId: goodsId, quantity: quantity });
  }
  res.send({ result: "success" });
});

module.exports = router;